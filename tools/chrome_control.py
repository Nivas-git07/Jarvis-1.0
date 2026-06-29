import asyncio
# IMPORT NOTICE: We pull ChatOllama directly from browser_use, NOT from langchain
from browser_use import Agent, ChatOllama

async def run_search():
    print("=== JARVIS TEXT-TO-ACTION ENGINE ===")
    
    user_prompt = "go to flipkart.com and search for a watch under 500"
    print(f"\nTask Input: '{user_prompt}'")
    print("\n[1/2] Loading native browser-use Ollama structure adapter...")
    
    # Using the built-in browser-use wrapper completely cleans up the schema translation layer
    llm = ChatOllama(
        model="qwen2.5-coder:7b",

    )

    print("[2/2] Spawning automated web controller agent...")
    agent = Agent(
        task=user_prompt,
        llm=llm
    )

    print("\n[3/3] Executing Action Loop...")
    try:
        result = await agent.run()
        print("\n=== ACTION COMPLETED BY JARVIS ===")
        print(result)
        
    except Exception as e:
        print(f"\n[Execution Failure]: {e}")

if __name__ == '__main__':
    asyncio.run(run_search())