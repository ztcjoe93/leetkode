
def isIsomorphic(s: str, t: str) -> bool:
    '''
    what are the conditions for 2 strings to be isomorphic?
    
    1. given a letter in s1, it is represented by a letter in s2 (i.e aab -> ccd (a->c, b->d))
    2. given a represented letter in s1, the indices must be the same in both s1 and s2
    True = (egg, add [e0g1g2, a0d1d2]), False = (foo, bar [f0o1o2, b0a1r2])
    '''
    
    letter_hm = {}
    mapped = set()
    
    for i in range(len(s)):
        if s[i] not in letter_hm:
            if t[i] in mapped:
                return False
            letter_hm[s[i]] = t[i]
            mapped.add(t[i])
        elif letter_hm[s[i]] != t[i]:
            return False
    
    return True
