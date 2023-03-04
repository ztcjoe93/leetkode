def isSubsequence(s: str, t: str) -> bool:
    cur = 0
    
    for i in range(len(t)):
        if cur == len(s):
            return True
        if t[i] == s[cur]:
            cur += 1
    if cur == len(s):
        return True
    return False
