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
            freq[x] = 0
            tracker.add(x)
    
    trackerList = list(tracker)
    if len(trackerList) == 0:
        print("True")
        return
    
    i = 0
    numDiff = 0
    while i <= len(trackerList)-2:
        firstVal = freq[trackerList[i]]
        secondVal = freq[trackerList[i+1]]
        if abs(firstVal - secondVal) > 1:
            print("False")
            return
        elif abs(firstVal - secondVal) == 1:
            numDiff += 1
            if numDiff > 1:
                print("False")
                return
        i+=1
    print("True")


cool("abcddee")