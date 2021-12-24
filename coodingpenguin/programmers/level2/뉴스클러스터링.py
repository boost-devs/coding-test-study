from collections import Counter


def create_set(s):
    s = s.lower()
    words = []
    for i in range(len(s) - 1):
        word = s[i : i + 2]
        if word.isalpha():
            words.append(word)
    return Counter(words)


def solution(str1, str2):
    set1 = create_set(str1)  # str1의 다중집합
    set2 = create_set(str2)  # str2의 다중집합

    inter = sum((set1 & set2).values())  # 두 다중집합의 교집합 크기
    union = sum((set1 | set2).values())  # 두 다중집합의 합집합 크기
    if not inter and not union:
        return 65536  # 교집합, 합집합이 공집한인 경우
    return int(inter / union * 65536)  # 자카드 유사도


if __name__ == "__main__":
    str1 = "FRANCE"
    str2 = "french"
    print(solution(str1, str2))
