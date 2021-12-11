def solution(record):
    user2nn = {}
    logs = []
    for line in record:
        op, user = line.split(' ', 1)
        if op != "Leave":
            user, nn = user.split()
            user2nn[user] = nn
            
        if op != "Change":
            logs.append((op[0], user))
            
    return [
        f"{user2nn[u]}님이 {'들어왔' if o == 'E' else '나갔'}습니다."
        for o, u in logs
    ]