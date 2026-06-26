import asyncio
from browser_use import Agent
from langchain_ollama import ChatOllama
from pydantic import Field

# 1. Custom class to satisfy the browser-use provider property check
class BrowserUseOllama(ChatOllama):
    provider: str = Field(default="ollama")
    
    model_config = {
        "extra": "allow"
    }

    @property
    def model_name(self):
        return self.model

async def run_search():
    print("=== JARVIS TEXT-TO-ACTION ENGINE ===")
    
    user_prompt = "go to flipkart.com and search for a watch under 500"
    print(f"\nTask Input: '{user_prompt}'")
    
    # 2. Initialize your local model with proper memory configuration
    llm = BrowserUseOllama(
        model="qwen2.5-coder:7b",
        base_url="http://127.0.0.1:11435",
        temperature=0.0,
        num_ctx=32000
    )

    print("[1/2] Spawning automated web controller agent...")
    
    # 3. Use 'tool_call_in_content=False' to stop structural parser errors
    agent = Agent(
        task=user_prompt,
        llm=llm,
        tool_call_in_content=False
    )

    print("\n[2/2] Executing Action Loop...")
    try:
        result = await agent.run()
        print("\n=== ACTION COMPLETED BY JARVIS ===")
        print(result)
        
    except Exception as e:
        print(f"\n[Execution Failure]: {e}")

if __name__ == '__main__':
    asyncio.run(run_search())