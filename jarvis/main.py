
#!/usr/bin/env python3
"""
Jarvis AI Agent - Main Entry Point

An autonomous desktop agent that can understand natural language commands,
execute tasks using tools, and maintain conversation memory.
"""

import asyncio

from core.session import SessionManager
from core.context import Context
from core.brain import Brain
from core.planner import Planner
from core.executor import Executor
from core.memory import MemorySystem
from core.registry import ToolRegistry
from llm.router import LLMRouter
from config.settings import Settings
from config.logging import get_logger
from config.prompts import Prompts

class Jarvis:
    """Main Jarvis AI Agent class"""
    
    def __init__(self):
        self.settings = Settings()
        get_logger("jarvis", self.settings.log_level)
        self.prompts = Prompts()
        
        # Initialize core components
        self.llm_router = LLMRouter()
        self.memory = MemorySystem()
        self.tool_registry = ToolRegistry()
        self.brain = Brain(self.llm_router, self.memory, self.prompts)
        self.planner = Planner(self.brain, self.prompts)
        self.executor = Executor(self.tool_registry, self.memory)
        
        # Initialize session
        self.session = SessionManager()
        self.session.create_session()
        
        # Create context
        self.context = Context(
            user_input="",
            memory=self.memory,
            tools=self.tool_registry,
            llm=self.llm_router,
            config=self.settings,
            session=self.session
        )
        self.context.session_id = self.session.session_id

        
        # Load tools
        self.tool_registry.load_tools()
    
    async def run(self):
        """Main agent loop"""
        print("🤖 Jarvis AI Agent is ready!")
        print("Type 'exit' to quit")
        print("-" * 50)
        
        try:
            while True:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                # Update context
                self.context.user_input = user_input
                
                # Run the agent loop
                await self._process_request(user_input)
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
        except Exception as e:
            print(f"Error: {e}")
    
    async def _process_request(self, user_input: str):
        """Process user request through the agent pipeline"""
        try:
            # Update session
            self.session.update_user_input(user_input)
            
            # Plan the task
            plan = await self.planner.create_plan(user_input, self.context)
            self.session.update_plan(plan)
            
            # Execute the plan
            result = await self.executor.execute_plan(plan, self.context)
            
            # Update memory with result
            await self.memory.store_interaction(
                user_input=user_input,
                plan=plan,
                result=result,
                session_id=self.session.session_id
            )
            
            # Generate response
            response = await self.brain.generate_response(
                user_input=user_input,
                plan=plan,
                result=result,
                context=self.context
            )
            
            print(f"\nJarvis: {response}")
            
        except Exception as e:
            error_msg = f"I encountered an error: {str(e)}"
            print(f"\nJarvis: {error_msg}")
            await self.memory.store_interaction(
                user_input=user_input,
                error=str(e),
                session_id=self.session.session_id
            )

async def main():
    """Main entry point"""
    jarvis = Jarvis()
    await jarvis.run()


if __name__ == "__main__":
    asyncio.run(main())
