from __future__ import annotations

import os

import requests
from dotenv import find_dotenv
from dotenv import load_dotenv

from src.utils import common

# Load Env Vars
_ = load_dotenv(find_dotenv())

# Load Config
CONFIG = common.config()

# Initialize Logger
logger = common.create_logger(__name__)

# Constants
AUTH_TOKEN = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
API_URL = CONFIG["github"]["api_url"]
OWNER = CONFIG["github"]["owner"]
REPO = CONFIG["github"]["repo"]
TIMEOUT = CONFIG["github"]["timeout"]


def _check_response(response: requests.Response) -> requests.Response:
    """
    Check the response from a HTTP request and raise an exception if it indicates an error.

    Args:
        response (requests.Response): The response object from the HTTP request.

    Raises:
        requests.exceptions.HTTPError: If the response status code is not 200.
        requests.exceptions.HTTPError: If the response body is empty.

    Returns:
        requests.Response: The response object from the HTTP request.
    """

    if response.status_code == 401:
        message = f"Request failed with status code {response.status_code}, check your auth token"
        logger.error(message)
        raise requests.exceptions.HTTPError(message)
        return

    if response.status_code == 404:
        message = f"Request failed with status code {response.status_code}, check your owner and repo"
        logger.error(message)
        raise requests.exceptions.HTTPError(message)
        return

    if response.status_code not in [200, 201]:
        message = f"Request failed with status code {response.status_code}"
        logger.error(message)
        raise requests.exceptions.HTTPError(message)
        return

    if not response.json():
        message = "Request succeeded but response body is empty, no issues found"
        logger.error(message)
        raise requests.exceptions.HTTPError(message)
        return

    return response


def get_issues(owner: str = OWNER, repo: str = REPO, api_url: str = API_URL) -> list[dict]:
    """
    Get the issues for a given repository.

    Args:
        owner (str, optional): The owner of the repository. Defaults to OWNER.
        repo (str, optional): The name of the repository. Defaults to REPO.
        api_url (str, optional): The base URL for the GitHub API. Defaults to API_BASE_URL.
            NOTE: Do not include a trailing slash.

    Returns:
        list[dict]: A list of issues for the given repository.

    Raises:
        ValueError: If the API_BASE_URL is invalid.
        ConnectionError: If the API_BASE_URL is unreachable.
    """
    try:
        request = requests.get(
            url=f"{API_URL}/repos/{owner}/{repo}/issues",
            headers={
                "Authorization": f"Bearer {AUTH_TOKEN}",
                "Accept": "application/vnd.github+json",
            },
            timeout=TIMEOUT,
        )
        request = _check_response(request)
        return request.json()
    except requests.exceptions.MissingSchema as e:
        message = f"Invalid URL: {API_URL}"
        logger.error(message)
        raise ValueError(message) from e
        return
    except requests.exceptions.ConnectionError as e:
        message = f"Unable to connect to {API_URL}"
        logger.error(message)
        raise ConnectionError(message) from e
        return


def create_comment_on_issue(
    issue_number: int,
    comment: str,
    owner: str = OWNER,
    repo: str = REPO,
    api_url: str = API_URL,
) -> dict:
    """
    Comment on a GitHub issue.

    Args:
        issue_number (int): The issue number.
        comment (str): The comment to post.
        owner (str, optional): The owner of the repository. Defaults to OWNER.
        repo (str, optional): The name of the repository. Defaults to REPO.
        api_url (str, optional): The base URL for the GitHub API. Defaults to API_BASE_URL.
            NOTE: Do not include a trailing slash.

    Returns:
        dict: The response from the GitHub API.

    Raises:
        ValueError: If the API_BASE_URL is invalid.
        ConnectionError: If the API_BASE_URL is unreachable.
    """

    try:
        url = f"{API_URL}/repos/{owner}/{repo}/issues/{issue_number}/comments"
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}", "Accept": "application/vnd.github+json"}
        data = {"body": comment}
        response = requests.post(url=url, headers=headers, json=data, timeout=TIMEOUT)
        _check_response(response)
        return response.json()
    except requests.exceptions.MissingSchema as e:
        message = f"Invalid URL: {API_URL}"
        logger.error(message)
        raise ValueError(message) from e
        return
    except requests.exceptions.ConnectionError as e:
        message = f"Unable to connect to {API_URL}"
        logger.error(message)
        raise ConnectionError(message) from e
        return
