pr = int(input("выручка фирмы: "))
сost = int(input("издержки фирмы: "))
if pr > сost:
    print("выручка больше издержек на: ", pr - сost)
else:
    print("издержки больше выручки на: ",сost - pr)