# LangGraph Template Project

A template structure for building applications with LangGraph and LangChain, providing a standardized foundation for graph-based language model applications.

## Overview

This project serves as a template for building LangGraph applications, offering a structured approach to organizing code, managing dependencies, and implementing an API layer. It combines the power of LangChain and LangGraph to create scalable and maintainable language model applications.


## Prerequisites

- Python 3.11 or newer (but less than 3.13)
- Poetry for dependency management

## Dependencies

### Main Dependencies
- FastAPI - Web framework for building APIs
- LangChain - Framework for developing applications powered by language models
- LangGraph - Graph-based operations for LangChain
- Uvicorn - ASGI server implementation
- ChromaDB - Vector database for embedding storage
- Langchain-Ollama - Integration with Ollama models
- Python-dotenv - Environment variable management

### Development Dependencies
- pytest - Testing framework
- black - Code formatter
- isort - Import sorter
- ruff - Fast Python linter
- pytest-asyncio - Async testing support

## Installation

1. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

1. Start the development server:
```bash
poetry run uvicorn app.main:app --reload
```

## Development

### Code Formatting

The project uses several tools to maintain code quality:

```bash
# Format code
poetry run black .

# Sort imports
poetry run isort .

# Run linter
poetry run ruff check .
```

### Running Tests

```bash
poetry run pytest
```
