inp = "Y4g2ke3A3BV9"

while inp:
    letter, num = "", ""
    if inp[0].isalpha():
        letter = inp[0]
        inp = inp[1:]
        if len(inp) != 0:
            while inp[0].isdigit():
                num += inp[0]
                if len(inp)!=1:
                    inp = inp[1:]
                else:
                    break

        if num == "":
            num = 1
        else:
            num = int(num)
        print(num * letter, end="")