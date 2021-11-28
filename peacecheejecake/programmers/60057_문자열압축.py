def solution(s):
    sl = len(s)
    min_len = sl
    for ss in range(1, sl):
        last_slice = s[:ss]
        cc = 1
        compressed = ''
        for i in range(ss, sl, ss):
            slice = s[i:i + ss]
            if slice == last_slice:
                cc += 1
            else:
                compressed += f"{cc if cc > 1 else ''}{last_slice}"
                last_slice = slice
                cc = 1
        
        compressed += f"{cc if cc > 1 else ''}{last_slice}"
        min_len = min(min_len, len(compressed))
    return min_len