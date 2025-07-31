from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from  dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], ## Ensure correct absolute path
                "transport":"stdio",
            },
            "weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable-http",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    
    tools=await client.get_tools()
    model=ChatGroq(model_name="llama3-8b-8192")
    agent=create_react_agent(
        model,tools
    )

    math_response=await agent.ainvoke(
        {"message":[{"role":"user","content":"What is 2+2?"}]}
    )

    print("Math Response:",math_response['messages'][-1].content)

asyncio.run(main())