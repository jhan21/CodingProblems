def isPalindrome(s):
    t = s.lower()
    whole = ""
    for i in range(len(t)):
        if t[i] >= "a" and t[i] <= "z" or t[i] >= "0" and t[i] <= "9":
            whole += t[i]
    
    for i in range(int(len(whole)/2)):
        if whole[i] != whole[len(whole)-i-1]:
            return False
    return True