from __future__ import annotations

import os

import requests
from dotenv import find_dotenv
from dotenv import load_dotenv

from src.utils import common

# Load Env Vars
_ = load_dotenv(find_dotenv())

# Constants
API_BASE_URL = "https://api.github.com"
AUTH_TOKEN = os.environ.get("GITHUB_AUTH_TOKEN")
OWNER = common.config()["github"]["owner"]
REPO = common.config()["github"]["repo"]


def get_issues(owner: str = OWNER, repo: str = REPO) -> dict:
    """
    Get the issues for a given repository.

    Args:
        owner (str, optional): The owner of the repository. Defaults to OWNER.
        repo (str, optional): The name of the repository. Defaults to REPO.

    Returns:
        dict: A dictionary containing the issues for the repository.
    """
    request = requests.get(
        url=f"{API_BASE_URL}/repos/{owner}/{repo}/issues",
        headers={
            "Authorization": f"Bearer {AUTH_TOKEN}",
            "Accept": "application/vnd.github+json",
        },
    )
    return request.json()
