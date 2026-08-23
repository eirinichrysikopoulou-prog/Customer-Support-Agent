# Customer Support Triage Agent

A LangGraph-based customer support system that classifies incoming tickets, routes them to specialized support agents, and generates responses using domain-specific RAG.

## Features

* Ticket classification by **category**, **urgency**, and **summary**
* Conditional routing with LangGraph
* Specialized **Billing**, **Technical**, and **General** support nodes
* RAG over category-specific knowledge bases
* Chroma vector store with Gemini embeddings
* Response evaluation with a confidence score
* Automatic resolution for high-confidence responses
* Human-review path for low-confidence responses

## Workflow

```text
Customer Ticket
      ↓
Classification
      ↓
Router
      ↓
Billing / Technical / General
      ↓
Domain-specific RAG
      ↓
Response Evaluation
      ↓
Confidence >= 0.75?
   ┌───────┴───────┐
  Yes              No
   ↓                ↓
Resolve        Human Review
```

## Tech Stack

* Python
* LangGraph
* LangChain
* Google Gemini API
* Chroma
* Pydantic

## Setup

Install the required dependencies and create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

API keys and other secrets should never be committed to the repository.

## Project Status

The core LangGraph workflow, specialist RAG pipelines, and confidence-based response evaluation are implemented. Human-in-the-loop escalation is being finalized.
