def solution(w, h):
    import math

    gcd = math.gcd(w, h)  # 최대공약수
    if gcd == 1:
        return w * h - (w + h - 1)
    return w * h - (w + h - gcd)
