from retriever import search_docs
from prompts import SYSTEM_PROMPT
from models import llm
from tools import run_tools

class AgentPipeline:
  def run(self, user_query):
    query = user_query.strip()
    context = search_docs(query)

    prompt = f"""
    {SYSTEM_PROMPT}
    Context:
    {context}
    User:
    {query}
    """

    response = llm.invoke(prompt)
    if response.requires_tool:
      tool_result = run_tools(response.tool_call)
      response = llm.invoke(
        f"Tool Result:\n{tool_result}\n\nAnswer the user."
      )
    return response.text

def clean_response(text):
  return text.strip()

def main():
  AgentPipeline()
  clean_response()

if __name__ == "__main__":
  main()