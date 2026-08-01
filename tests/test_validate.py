import pytest  
from validate import validate_action
from agent import AIAgent
import time

def test_agent_intialisation():
  agent = AIAgent()
  assert agent is not None
  assert agent.name == "Operational-Exception-Triage-Agent"

def test_basic_response(mocker):
  mock_search = mocker.patch(
    "agent.search_tool"
  )

  agent = AIAgent()

  start = time.time()

  response = agent.query(
    "What is the capital of Spain?"
  )

  mock_search.assert_called_once()
  assert len(response) > 0
  assert "answer" in response
  assert "confidence" in response
  assert isinstance(
    response["confidence"],
    float
  )
  duration = time.time() - start
  assert duration < 10

def test_agent_handles_unknown_question():
  agent = AIAgent()
  response = agent.query(
    "Tell me something you do not know?"
  )

  assert (
    "I don't know" in response 
    or 
    "I do not have enough information" in response
  )
  assert "answer" in response

def test_complex_tasks():
  agent = AIAgent()
  response = agent.run(
    """
    Analyse the .csv files,
    identify problems,
    and suggest solutions.
    """
  )
  assert ".csv files" in response
  assert "problem" in response
  assert "solutions" in response

def test_empty_input():
  agent = AIAgent()
  with pytest.raises(ValueError):
    agent.run("")

def test_previous_bug_case():
  agent = AIAgent()
  response = agent.run(
    "Old failing prompt"
  )
  expected_output = "Old failing prompt"
  assert response == expected_output

def test_valid_action():
  assert validate_action({
    "action": "query",
    "query": "latest material",
  })

def test_missing_action():
  assert validate_action({
    "action": "query",
    "query": "material id"
  })

def test_missing_material():
  assert not validate_action({
    "action": "search"
  })

def main():
  test_valid_action()
  test_missing_action()
  test_missing_material()
  test_agent_intialisation()
  test_basic_response()
  test_agent_handles_unknown_question()
  test_complex_tasks()
  test_empty_input()
  test_previous_bug_case()

if __name__ == "__main__":
  main()