import json
import requests
import argparse


class ReviewAPI:
    def __init__(self, token: str, owner: str, repo: str, id: int):
        self.headers = {"Authorization": f"token {token}"}
        self.owner = owner
        self.repo = repo
        self.id = id

    def has_no_reviewer(self):
        query = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{self.id}/requested_reviewers"
        response = requests.get(query, headers=self.headers)
        num_of_reviewers = len(response.json()["users"])
        if not num_of_reviewers:
            return True
        return False

    def get_reviewers(self, file_name: str):
        with open(file_name, "r") as f:
            info = json.load(f)
            pointer = info["pointer"]  # 시작 포인터
            rotation = info["rotation"]  # 로테이션 명수
            members = info["members"]  # 팀원 리스트

            return members[pointer : pointer + rotation]

    def set_reviewers(self):
        reviewers = self.get_reviewers("./.scripts/reviewer_info.json")
        query = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{self.id}/requested_reviewers"
        data = {"reviewers": reviewers}
        response = requests.post(query, headers=self.headers, data=json.dumps(data))


owner = "boostcamp-ai-tech-4"
repo = "github-action-test"

parser = argparse.ArgumentParser()
parser.add_argument("--token", type=str, default=None, help="github access token")
parser.add_argument("--id", type=int, default=None, help="pull request number")

args = parser.parse_args(description="Get Pull Request Information")
access_token = args.token
id = args.id

reviewApi = ReviewAPI(access_token, owner, repo, id)
if reviewApi.has_no_reviewer():
    reviewApi.set_reviewers()
