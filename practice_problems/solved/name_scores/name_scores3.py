def main():
    try:
        print(totalNameScore(getCleanedNames()))
    except:
        print("names.txt missing or invalid input")

def getCleanedNames():
    names = sorted(open('names.txt').readline().split(','))
    return [name[1:-1] for name in names]

def totalNameScore(names):
    nameValue = [sum([ord(c)-ord('A')+1 for c in word]) for word in names]
    return sum([t[0]*t[1] for t in enumerate(nameValue, start=1)])

main()