from __future__ import annotations

from dotenv import find_dotenv
from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.tools import StructuredTool
from langchain_community.chat_models import ChatOpenAI

from src.github import issues
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


llm = ChatOpenAI(model_name=MODEL, temperature=TEMPERATURE)


def comment_on_github_issue(issue_number: int, comment: str) -> str:
    """Agent Tool to comment on a GitHub Issue.

    Args:
        issue_number (int): The issue number to comment on.
        comment (str): The comment to post on the issue.
    """
    issues.create_comment_on_issue(issue_number, comment)
    return "Commented on GitHub Issue"


tool = StructuredTool.from_function(comment_on_github_issue)

agent_executor = initialize_agent(
    [tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

issue = issues.get_issues()[0]
task_prompt = """Act as Project Manager, break down the following task
and assign role (i.e.: Python Developer, Frontend Developer, etc.) to each subtask.
Comment the result on GitHub."""
user_input = f"""{task_prompt} Task:```
Number: {issue['number']}\n\nTitle: {issue['title']}\n\n Description: {issue['body']}
```
"""
agent_executor.invoke({"input": f"{user_input}"})
