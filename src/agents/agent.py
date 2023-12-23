from __future__ import annotations

from typing import Any
from typing import Callable

from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain_core.language_models.chat_models import BaseChatModel


class Agent:
    def __init__(
        self,
        llm: BaseChatModel,
        tools: list[Callable[..., str]],
        prompt: str,
        type: AgentType,
        verbose: bool = True,
    ):
        """Initialize an Agent.

        Args:
            llm (BaseChatModel): The language model used by the agent.
            tools (list[Callable[..., str]]): The list of tools available to the agent.
            prompt (str): The prompt used by the agent.
            type (AgentType): The type of the agent.
            verbose (bool, optional): Whether to enable verbose mode. Defaults to True.
        """
        self._llm = llm
        self._tools = tools
        self._prompt = prompt
        self._type = type
        self._verbose = verbose
        self._executor = initialize_agent(tools=self.tools, llm=self.llm, agent=self.type, verbose=self.verbose)

    @property
    def llm(self) -> BaseChatModel:
        """Get the Agent's LLM."""
        return self._llm

    @llm.setter
    def llm(self, llm: BaseChatModel) -> None:
        """Set the Agent's LLM."""
        self._llm = llm

    @property
    def tools(self) -> list[Callable[..., str]]:
        """Get the Agent's Tools."""
        return self._tools

    @tools.setter
    def tools(self, tools) -> None:
        """Set the Agent's Tools."""
        self._tools = tools

    @property
    def type(self) -> AgentType:
        """Get the Agent's Type."""
        return self._type

    @type.setter
    def type(self, type: AgentType) -> None:
        """Set the Agent's Type."""
        self._type = type

    @property
    def prompt(self) -> str:
        """Get the Agent's Prompt."""
        return self._prompt

    @prompt.setter
    def prompt(self, prompt: str):
        """Set the Agent's Prompt."""
        self._prompt = prompt

    @property
    def verbose(self) -> bool:
        """Get the Agent's Verbose."""
        return self._verbose

    @verbose.setter
    def verbose(self, verbose: bool) -> None:
        """Set the Agent's Verbose."""
        self._verbose = verbose

    def invoke(self, user_input: str) -> dict[str, Any]:
        """Invoke the Agent.

        Args:
            user_input (str): The user input to the agent.

        Returns:
            dict: The response from the agent.
        """
        if self.prompt:
            user_input = f"{self.prompt} Task: ```{user_input}```"
        return self._executor.invoke(user_input)
