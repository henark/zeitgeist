import os
from github import Github, Auth
from github.GithubException import BadCredentialsException

GH = Github(os.getenv("ZERO_GITHUB_TOKEN"))
REPO = None

try:
    REPO = GH.get_repo("Aurumgrid/Z-n-")
except BadCredentialsException:
    print("Warning: Bad GitHub credentials. GitHub integration will be disabled.")
except Exception as e:
    print(f"An unexpected error occurred while connecting to GitHub: {e}")


def open_pr(branch_name: str, title: str, body: str):
    if not REPO:
        print("Error: Cannot open pull request, GitHub repository not available.")
        return

    try:
        pr = REPO.create_pull(
            title=title,
            body=body,
            head=branch_name,
            base=REPO.default_branch,
        )
        print(f"Pull request opened: {pr.html_url}")
        return pr
    except Exception as e:
        print(f"Failed to open pull request: {e}")
        return None
