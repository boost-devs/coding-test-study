import json


def load_json(file_path):
    info = None
    with open(file_path, "r") as f:
        info = json.load(f)
    print("Load and parse reviewer_info.json")
    return info


def change_reviewer(info):
    pointer = info["pointer"]  # 시작 포인터
    total = info["total"]  # 총 명수
    rotation = info["rotation"]  # 로테이션 명수
    members = info["members"]  # 팀원 리스트

    info["pointer"] = (pointer + rotation) % total  # 포인터 변경
    print("This week reviewer:", *members[pointer : pointer + rotation])
    return info


def save_json(file_path, info):
    with open(file_path, "w") as f:
        json.dump(info, f)
    print("Save changed info in reviewer_info.json")


file_path = "reviewer_info.json"
info = load_json(file_path)
info = change_reviewer(info)
save_json(file_path, info)
