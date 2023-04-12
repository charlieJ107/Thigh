
inputCode = "124523461"
s = None

theDict = {'1': 'A', '2': 'B', '3': 'C'}
newCode = 4
for k in inputCode:

    output = theDict[k]
    print(output)

    if s != None:
        theDict[str(newCode)] = s+theDict[k][0]
        newCode+=1
        s=None

    s = output
