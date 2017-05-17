def main():
    try:
        print(totalNameScore(getCleanedNames()))
    except:
        print("names.txt missing or invalid input")

def getCleanedNames():
    return sorted([s[1:-1] for s in open('names.txt').readline().split(',')])

def totalNameScore(names):
    points = dict([(chr(ord('A')+i), i+1) for i in range(26)])
    nameWorths = [sum([points[c] for c in name]) for name in names]
    return sum([t[0]*t[1] for t in enumerate(nameWorths, start=1)])

main()


