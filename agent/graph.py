from dotenv import load_dotenv
load_dotenv()
from langchain.globals import set_verbose, set_debug
from langchain_groq import ChatGroq
from states import *
from prompts import *
from langgraph.graph import StateGraph
llm = ChatGroq(model="openai/gpt-oss-120b")
set_debug(True)
set_verbose(True)
def planner_agent(state:dict) -> dict:
    resp = llm.with_structured_output(Plan).invoke( planner_prompt(state["user_prompt"]))
    return resp


user_prompt = "create a simple calculator web application"

graph = StateGraph(dict)
graph.add_node("planner", planner_agent)
graph.set_entry_point("planner")
agent = graph.compile()
result = agent.invoke({"user_prompt":user_prompt})


resp = llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
print(resp)
