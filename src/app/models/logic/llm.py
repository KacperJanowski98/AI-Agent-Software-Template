from langchain_ollama import ChatOllama

from app.models.logic.tools.weather import get_weather


def create_llm(model_name: str = "qwen2.5:14b") -> ChatOllama:
    """
    Factory function to create and configure the LLM model with the provided tools.

    Args:
        model_name (str): The name of the language model to use.

    Returns:
        ChatOllama: The configured LLM instance.
    """
    tools = [get_weather]
    model = ChatOllama(model=model_name)
    model = model.bind_tools(tools)
    return model
