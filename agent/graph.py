from sys import implementation

from langgraph.graph import StateGraph
from dotenv import load_dotenv
load_dotenv()
from langchain.globals import set_verbose, set_debug
from langchain_groq import ChatGroq
from langgraph.constants import END
from agent.prompts import *
from agent.states import *
from agent.tools import *
from langgraph.prebuilt import create_react_agent

llm = ChatGroq(model="openai/gpt-oss-120b")
set_debug(True)
set_verbose(True)
def planner_agent(state:dict) -> dict:
    resp = llm.with_structured_output(Plan).invoke( planner_prompt(state["user_prompt"]))
    return {"plan": resp }

def architect_agent(state:dict) -> dict:
    res = (llm.with_structured_output(ImplementationSteps).
           invoke(architect_prompt(state["plan"])))
    res.plan = state["plan"]
    return { "implementation_steps" : res}

def coder_agent(state:dict) -> dict:
    current_task = state["implementation_steps"].tasks[0]
    existing_content = read_file.run(current_task.filepath)

    system_prompt = coder_system_prompt()
    user_prompt = (
        f"Task: {current_task.description}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content:\n{existing_content}\n"
        "Use write_file(path, content) to save your changes."
    )
    coder_tools = [read_file, write_file, list_files, get_current_directory]
    react_agent = create_react_agent(llm, coder_tools)

    react_agent.invoke({"messages": [{"role": "system", "content": system_prompt},
                                     {"role": "user", "content": user_prompt}]})

    return {}
user_prompt = "create a simple calculator web application"

graph = StateGraph(dict)
graph.add_node("planner", planner_agent)
graph.add_node("architect", architect_agent)
graph.add_node("coder", coder_agent)
graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.set_entry_point("planner")

agent = graph.compile()
result = agent.invoke({"user_prompt":user_prompt})


print(result)
