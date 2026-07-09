import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from .tools import tools_list

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile", # Naya supported model
    temperature=0
)

# Define the system prompt as a SystemMessage object
system_prompt = SystemMessage(
    content="""You are an AI CRM assistant for life science reps. 
Extract information from user chat and use your tools to log or edit database entries.
Do not ask the user to fill forms manually. Always trigger the appropriate tool."""
)

# LangGraph ke naye version ke hisaab se sirf 'prompt' use karna hai
agent_executor = create_react_agent(
    model=llm, 
    tools=tools_list, 
    prompt=system_prompt  
)

def process_chat(message: str, thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    
    # We pass the user message here
    result = agent_executor.invoke(
        {"messages": [("user", message)]}, 
        config=config
    )
    
    # Return the final content from the AI
    return result["messages"][-1].content