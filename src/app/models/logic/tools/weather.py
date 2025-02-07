from langchain_core.tools import tool


@tool
def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["warsaw"]:
        return "It's 15 degrees Celsius and cloudy."
    else:
        return "It's 32 degrees Celsius and sunny."
