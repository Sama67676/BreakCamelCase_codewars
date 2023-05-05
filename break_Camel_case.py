def solution(s):
    array=[]
    for i in range(len(s)):
        if s[i].isupper() and i>0:
            array.append(" " + s[i])
        else: 
            array.append(s[i])

    arr=("".join(array))
    return arr
#or
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

#or
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)


s=input("Enter here: ")
print(solution(s))