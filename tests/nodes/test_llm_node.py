import pytest

from unittest.mock import AsyncMock, MagicMock, patch
from langchain_core.messages import AIMessage

from app.nodes_edges.nodes.llm_node import llm_node


@patch("app.nodes_edges.nodes.llm_node.create_llm")
@pytest.mark.asyncio
async def test_llm_node(mock_create_llm, state):
    """Test the async llm_node function with a mocked LLM"""
    mock_llm = AsyncMock()
    mock_response = AsyncMock()
    mock_response.content = "Mocked AI response"
    mock_llm.ainvoke.return_value = mock_response
    mock_create_llm.return_value = mock_llm

    mock_promt = MagicMock()
    mock_promt.messages = state["messages"]
    state["prompt"] = mock_promt

    result = await llm_node(state)

    assert result["answer"] == "Mocked AI response"
    assert result["messages"][-1] == AIMessage(content="Mocked AI response")
    mock_llm.ainvoke.assert_called_once_with(state["messages"])
    mock_create_llm.assert_called_once()
