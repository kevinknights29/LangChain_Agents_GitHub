from __future__ import annotations

import json

from src.github import issues


def main():
    # test issues
    response = issues.get_issues()
    print("Get Issues: ", json.dumps(response, indent=" " * 4), sep="\n")


if __name__ == "__main__":
    main()
