#Question 1 Bloomberg interview 1 Cool words
#given a string "aaabbb" if all letters occur the same amount of times return true
#if you can remove 1 letter and have a cool word then return true also

def cool(string):
    freq = {}
    tracker = set()

    for x in string:
        if x in tracker:
            freq[x] += 1
        else:
            freq[x] = 1
            tracker.add(x)
    
    trackerList = sorted(list(tracker))
    if len(trackerList) == 0:
        print("True")
        return
    
    i = 0
    numDiff = 0
    while i < len(trackerList)-1:
        firstVal = freq[trackerList[i]]
        secondVal = freq[trackerList[i+1]]
        if (firstVal != secondVal) and (firstVal == 1):
            numDiff += 1
            if numDiff > 1:
                print("False")
                return
        elif abs(firstVal - secondVal) >= 1:
            print("False")
            return
        i+=1
    print("True")


cool("abbcc")
cool("a")
cool("aaa")
cool("abbbbcccc")
cool("aaabbbcc")
cool("aaabbbbc")
cool("abbbbbbbbbbbbbb")
cool("aabbbbbbbbbbbbbbbbbbbbbbbbb")
cool("abbccc")