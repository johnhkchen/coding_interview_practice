def main():
        try:
                print(totalNameScore(getNames()))
        except:
                print("names.txt missing, or invalid format")

def getNames():
        dirtyNames = open('names.txt').readline().split(',')
        # Trim double quotes
        trim = lambda s: s[1:-1]
        return sorted(map(trim, dirtyNames))

def totalNameScore(names):
        scoreCard = getScoreCard()
        atoi = lambda c: scoreCard[c]
        nameScore = lambda i: (i+1)*sum(map(atoi, names[i]))
        return sum(map(nameScore, range(len(names))))

def getScoreCard():
        # Create lookup dictionary of {A:1, B:2, ..., Z:26}
        score = lambda n: (chr(ord('A')+n), n+1)
        return dict(map(score, range(26)))

main()