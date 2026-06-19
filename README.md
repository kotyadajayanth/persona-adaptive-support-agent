# Persona Adaptive Customer Support Agent

## Project Overview

This project is an AI-powered customer support agent that adapts its responses based on customer personas. The system uses Retrieval Augmented Generation (RAG) to retrieve relevant information from a support knowledge base and generates persona-specific responses using Gemini.

## Features

* Persona Detection

  * Technical Expert
  * Frustrated User
  * Business Executive

* Knowledge Base Retrieval using ChromaDB

* Adaptive Response Generation

* Human Escalation System

* Human Handoff Summary

* Streamlit User Interface

## Architecture

User Query

↓

Persona Detection

↓

Knowledge Base Retrieval

↓

Response Generation

↓

Escalation Check

↓

Human Handoff Summary

## Tech Stack

* Python 3.11
* Gemini 2.5 Flash
* ChromaDB
* Streamlit
* Google GenAI SDK
* Python Dotenv

## Project Structure

data/

* Support documents

src/

* classifier.py
* rag.py
* generator.py
* escalation.py

app.py

README.md

requirements.txt

## Example Queries

1. How can I reset my password?

2. My API authentication is failing with a 401 error.

3. How does this issue impact business operations?

4. I want a refund for duplicate billing charges immediately.

## Escalation Logic

The system escalates conversations when:

* Billing issues are detected
* Refund requests are detected
* Legal issues are detected
* Retrieval confidence is low

## Future Improvements

* Multi-turn conversation memory
* Better persona classification
* PDF document ingestion
* Analytics dashboard
* Feedback collection system
