# LangChain_Agents_GitHub

This project aims to build LLM agents that can generate code for GitHub Issues using LangChain Agents

## Topics

1. [Overview](#overview)
2. [Goals](#goals)
3. [Scope and Context](#scope-and-context)
4. [System Design](#system-design)
5. [Alternatives Considered](#alternatives-considered)
6. [Learning Logs](#learning-logs)
7. [Resources](#resources)

---

## Current Results

### Agent Executor

#### Now it can perform multiple actions

![image](https://github.com/kevinknights29/LangChain_Agents_GitHub/assets/74464814/f5cbe315-c252-4301-9adc-ab306684d079)

### Output from Agent Action

![image](https://github.com/kevinknights29/LangChain_Agents_GitHub/assets/74464814/a0a250e1-da1b-45a4-8fb4-f370c8e1c844)

## Overview

`LangChain_Agents_GitHub` is an innovative project that leverages the capabilities of Large Language Models (LLMs) to interact with and resolve GitHub issues.
The project employs LangChain Agents, a framework designed to streamline the development of intelligent agents, to interpret, analyze, and generate code snippets in response to specific queries or problems presented in GitHub Issues.

## Goals

- Automate Code Generation: To develop LLM agents capable of generating accurate and efficient code solutions for problems described in GitHub issues.

- Improve Developer Workflow: To assist developers by reducing the time spent on routine issues, enabling them to focus on more complex tasks.

- Enhance Accuracy and Relevance: To ensure the generated code is not only syntactically correct but also contextually relevant to the issue at hand.

- Iterative Learning: To create a system that learns from past interactions to improve future code generation.

## Scope and Context

The project is focused on the development environment, particularly targeting developers and teams using GitHub as their primary version control system.
It aims to integrate seamlessly with GitHub's issue tracking system, providing an automated assistant for resolving coding issues.
The context of the project is highly technical, requiring a deep understanding of software development practices, GitHub's API, and LLM capabilities.

## System Design

The system is designed around the core LangChain Agent framework, which facilitates the integration of LLMs into the code generation process. Key components include:

- Issue Parser: Interprets and extracts relevant information from GitHub issues.

- LLM Integration: Connects with LLMs like GPT-4 for generating code based on the parsed issue data.

- Code Validator: Ensures the generated code is syntactically correct and meets basic quality standards.

- GitHub API Integration: Automates the process of responding to issues with generated code.

## Alternatives Considered

- Different LLMs: Evaluating various LLMs for their suitability in this context, including GPT-3 and Codex.

- Manual Code Review Integration: Incorporating a human-in-the-loop for validating generated code before submission.

- Use of Static Code Analyzers: To enhance the validation process by integrating static code analysis tools.

## Learning Logs

| Date | Learning |
|------|----------|
| 2023/12/23 | GPT-4 performs better reasoning than GPT-3, cost increase vs quality impact should be compared |
| 2023/12/23 | Using the `initialize_agent` function works better for multi input agents |
| 2023/12/23 | You can model agents with class since they consist of the same core elements |
| 2023/12/24 | Agent can perform multiple tasks on a single chain |

## Resources

- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [Passing Functions with Multiple Args to Agents](https://python.langchain.com/docs/modules/agents/tools/multi_input_tool)
- [GitHub Issues API](https://docs.github.com/en/rest/issues/comments?apiVersion=2022-11-28)
- [Function Type Hints Anotation](https://docs.python.org/3/library/typing.html#annotating-callable-objects)
