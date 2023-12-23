from __future__ import annotations

from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.agents.openai_assistant import OpenAIAssistantRunnable

from src.utils import common

# Load Env Vars
_ = load_dotenv(find_dotenv())

# Load Config
CONFIG = common.config()

# Initialize Logger
logger = common.create_logger(__name__)

# Constants
MODEL = CONFIG["openai"]["model"]
TEMPERATURE = CONFIG["openai"]["temperature"]

interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
    name="python assistant",
    instructions="""You are a Senior Software Engineer specialized in Python.
    Write the code and tests to complete a given task.""",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)
output = interpreter_assistant.invoke({"content": "What's 10 - 4 raised to the 2.7"})
output
