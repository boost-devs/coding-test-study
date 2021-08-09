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
        print("GET Requested Reviewers:", response.status_code)
        num_of_reviewers = len(response.json()["users"])
        print("Pull Request #{self.id} has {num_of_reviewers} reviewers")
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
        print("Reviewers List:", *reviewers)
        query = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{self.id}/requested_reviewers"
        data = {"reviewers": reviewers}
        response = requests.post(query, headers=self.headers, data=json.dumps(data))
        print("POST Requested Reviewers:", response.status_code)


owner = "boostcamp-ai-tech-4"
repo = "github-action-test"

parser = argparse.ArgumentParser(description="Get Pull Request Information")
parser.add_argument("--token", type=str, default=None, help="github access token")
parser.add_argument("--id", type=int, default=None, help="pull request number")

args = parser.parse_args()
access_token = args.token
id = args.id
print(f"New Pull Request Created #{id}")

reviewApi = ReviewAPI(access_token, owner, repo, id)
if reviewApi.has_no_reviewer():
    print(f"Pull Request #{id} has no reviewers requested")
    reviewApi.set_reviewers()
