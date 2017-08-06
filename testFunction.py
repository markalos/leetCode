def shortestPalindrome(s):
    newS = ""
    tpS = s
    for c in s:
        newS += "#" + c
    newS += "#"
    s = newS
    center, maxR = 0, 0
    ans = [0] * len(s)
    for i in range(len(s)):
        if(i < maxR):
            if(ans[2 * center - i] <= maxR - i):
                ans[i] = ans[2 * center - i]
            else:
                ans[i] = maxR - i + 1
                tpR = maxR + 1
                while(tpR < len(s) and 2 * i >= tpR):
                    if(s[tpR] == s[2 * i - tpR]):
                       tpR += 1
                       ans[i] += 1
                    else:
                       break
                tpR -= 1
                if(tpR > maxR + 1):
                       maxR = tpR
                       center = i
        else:
            ans[i] = 1
            tpR = i + 1
            while(tpR < len(s) and 2 * i >= tpR):
                if(s[tpR] == s[2 * i - tpR]):
                   tpR += 1
                   ans[i] += 1
                else:
                   break
            tpR -= 1
            if(tpR > maxR + 1):
                maxR = tpR
                center = i
    idx = 0
    for i in range(len(s) - 1, -1, -1):
        if(ans[i] == i + 1):
            idx = i
            break
    print(idx)
    return tpS[:ans[idx] - 2 - len(tpS): -1] + tpS
print(shortestPalindrome("aacecaaa"))
