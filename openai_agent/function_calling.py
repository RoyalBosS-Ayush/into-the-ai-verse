from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

load_dotenv()


@function_tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers
    """
    return a * b


agent = Agent(
    name="Math Agent",
    instructions="Always use your tools to solve math problems.",
    tools=[multiply],
    model="gpt-4o-mini",
)

response = Runner.run_sync(agent, "What's 2.3 times 3.2")
print(response.final_output)
