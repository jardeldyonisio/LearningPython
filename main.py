
VALUEKEYMARKET = 11.70
VALUEKEYREFINED = 46.33
STEAMTAX = 0.156
EUROTRUCKPRICEPACK = 7.55
EUROTRUCKSETCARDS = 7
MEDIANPRICEPROFIT = 0.17

def calcProfit ():
    qta = (VALUEKEYREFINED/EUROTRUCKPRICEPACK)*7
    print(qta)
    bruto = qta * MEDIANPRICEPROFIT
    print(bruto)
    return bruto - VALUEKEYMARKET

if __name__ == '__main__':
    test = calcProfit()
    print(test)
    