from __future__ import annotations

import json

from src.github import issues


def main():
    # test issues
    issues_response = issues.get_issues()
    print("Get Issues: ", json.dumps(issues_response, indent=" " * 4), sep="\n")
    issue = issues_response[0]
    issue_number = issue["number"]
    comment_response = issues.create_comment_on_issue(issue_number=issue_number, comment="Test Comment")
    print("Create Comment on Issue: ", json.dumps(comment_response, indent=" " * 4), sep="\n")


if __name__ == "__main__":
    main()
