def toWord(num):
        if num > 0 and num < 20:
                return {
                        1: 'one',
                        2: 'two',
                        3: 'three',
                        4: 'four',
                        5: 'five',
                        6: 'six',
                        7: 'seven',
                        8: 'eight',
                        9: 'nine',
                        10: 'ten',
                        11: 'eleven',
                        12: 'twelve',
                        13: 'thirteen',
                        14: 'fourteen',
                        15: 'fifteen',
                        16: 'sixteen',
                        17: 'seventeen',
                        18: 'eighteen',
                        19: 'nineteen'
                }[num]
        elif num >= 20 and num < 100:
                return {
                        2: 'twenty',
                        3: 'thirty',
                        4: 'forty',
                        5: 'fifty',
                        6: 'sixty',
                        7: 'seventy',
                        8: 'eighty',
                        9: 'ninety'
                }[int(num/10)]+toWord(num%10)
        elif num >= 100 and num < 1000:
                if (num % 100 != 0):
                        return toWord(int(num/100))+'hundredand'+toWord(int(num%100))
                else:
                        return toWord(int(num/100))+'hundred'
        elif num == 1000:
                return 'onethousand'
        else:
                return ''

print("Letters used: {}.".format(sum(map(len, map(toWord, range(1, 1000+1))))))