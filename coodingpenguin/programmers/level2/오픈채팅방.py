def solution(records):
    nickname_map = {}   # uid와 닉네임 매핑
    logs = []   # 처리된 로그
    for record in records:
        command, *rest = record.split()
        if command == 'Enter':
            nickname_map[rest[0]] = rest[1]
            logs.append((command, rest[0]))
        elif command == 'Change':
            nickname_map[rest[0]] = rest[1]
        else:
            logs.append((command, rest[0]))
    
    result = []
    for command, uid in logs:
        if command == 'Enter':
            result.append(f'{nickname_map[uid]}님이 들어왔습니다.')
        else:
            result.append(f'{nickname_map[uid]}님이 나갔습니다.')
    return result            