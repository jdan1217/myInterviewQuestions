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

    numDif = 0

    sortDict = sorted(freq.items(), key=lambda x:x[1])
    l = 0
    r = len(sortDict) - 1

    while l <= r:
        if sortDict[l][1] == sortDict[r][1]:
            print("True")
            return
        else:
            if sortDict[r][1] - 1 != sortDict[l][1] and sortDict[l][1] - 1 != 0:
                print("False")
                return
            
            elif sortDict[r][1] - 1 == sortDict[l][1] and sortDict[l][1] - 1 == 0:
                if sortDict[r-1][1] == sortDict[r][1]:
                    l+=1
                else:
                    r-=1
                numDif+=1

            elif sortDict[l][1] - 1 == 0:
                l += 1
                numDif += 1
            elif sortDict[r][1] - 1 == sortDict[l][1]:
                r -= 1
                numDif += 1
            if numDif > 1:
                print("False")
                return

    print("True")
    return

cool("a")
cool("ab")
cool("abc")
cool("abbcc")
cool("abbc")
cool("abbbccc")
cool("aabbeef")
cool("abbbcccc")
cool("abbccc")
cool("aabbbc")
