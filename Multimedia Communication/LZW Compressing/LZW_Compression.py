origin = "ABABBABCABABBA"
print("Origin is ", origin, ". This string has ", len(origin), "characters.")

w = 4
s = origin[0] # 将s初始化为第一个字符
theDict = {'A':1, 'B':2, 'C':3} #初始字典
charCount = 0 #计数压缩后的字符
print("The compressed string is:")
for c in origin[1:]:
    if s+c in theDict.keys(): # 判断S+C是否在字典中
        s = s+c
    else:
        print(theDict[s]) # 输出当前前缀s对应的码字w
        charCount+=1
        theDict[s+c] = w
        w += 1
        s = c
print(theDict[s])
print("The compressed string has ", charCount, "characters.")

