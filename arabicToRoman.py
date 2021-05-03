def romanize (k):
    units = k % 10
    tens = (k-units) % 100 // 10
    hundreds = (k-tens-units) % 1000 // 100
    thousands = (k//1000)

    uni_dict = {1: "I", 5: "V"}
    ten_dict = {1: "X", 5: "L"}
    hun_dict = {1: "C", 5: "D"}
    tho_dict = {1: "M", 5: "U"}

    LD = [uni_dict, ten_dict, hun_dict, tho_dict]
    POW = [units, tens, hundreds, thousands]
    rom = ""

    i = 3
    while i >= 0:
        if 0 < POW[i] < 4:
            rom = rom + LD[i][1]*POW[i]
        elif POW[i] == 4:
            rom = rom + LD[i][1] + LD[i][5]
        elif 4 < POW[i] < 9:
            rom = rom + LD[i][5] + (LD[i][1]*(POW[i]-5))
        elif POW[i] == 9:
            if i < 3:
                rom = rom + LD[i][1] + LD[i+1][1]
            else:
                rom = rom + 'UMMMM'
        i = i - 1
    return rom


n = int(input("Enter your number: "))
print(romanize(n))
