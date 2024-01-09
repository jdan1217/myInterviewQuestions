#Return Deepest nested string whithin balanced brackets
#ex ab{a} -> a |  {{a{b}c}} -> a | {a}{{b}}{{{c}}} -> c

def deepestStr(string):
    curHeight = 0
    currStr = ''
    maxHeight = float('-inf')
    stringAtMaxHeight = ''

    for x in string:
        if x == '{' or x == '[' or x == '(':
            curHeight += 1
            currStr = ''
        elif x == '}' or x == ']' or x == ')':
            if currStr != '' and curHeight > maxHeight:
                stringAtMaxHeight = currStr
                currStr = ''
                maxHeight = curHeight
            curHeight -= 1
        else:
            currStr += x

    print(stringAtMaxHeight)

deepestStr("{a}{{b}}{{{c}}}")
        
        