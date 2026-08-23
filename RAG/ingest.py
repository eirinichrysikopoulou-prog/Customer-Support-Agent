import tempfile
from functools import lru_cache


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from schemas import Category
from llm import llm
from langchain_community.document_loaders import PyPDFLoader

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)
KNOWLEDGE_PATH = Path(__file__).parent / "knowledge"
def read_file(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return file_path.read_text(encoding="cp1252")

@lru_cache
def create_kb(category: Category) -> Chroma:

    category_path = KNOWLEDGE_PATH / category

    if not category_path.exists():
        raise ValueError(
            f"Knowledge base for category '{category}' does not exist."
        )

    docs = []

    for file_path in category_path.iterdir():

        if not file_path.is_file():
            continue

        # Only process PDFs
        if file_path.suffix.lower() != ".pdf":
            continue

        loader = PyPDFLoader(str(file_path))

        pdf_docs = loader.load()

        # Add our own metadata to each page
        for doc in pdf_docs:
            doc.metadata["category"] = category
            doc.metadata["source"] = file_path.name

        docs.extend(pdf_docs)

    if not docs:
        raise ValueError(
            f"No PDF documents found for category '{category}'."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=tempfile.mkdtemp()
    )

    return vector_store


def create_rag_chain(category: Category):

    vector_store=create_kb(category)
    retriever= vector_store.as_retriever(search_type="similarity",search_kwargs={"k":3})
    prompt= ChatPromptTemplate.from_template("Answer the question based only on the following context: {context} Question: {question}. Make sure you answer in a concise manner and if you don't know the answer just say""I don't know"
                                             )
    def format_docs(docs):
        return"\n\n".join([doc.page_content for doc in docs])

    rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
    )

    return rag_chain





