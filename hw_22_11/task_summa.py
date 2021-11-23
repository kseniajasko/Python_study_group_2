
def summa_in_money(summa):
    money_dict = {}
    penny_dict = {}
    if summa > 0:
        number = round(summa, 1)
        int_number = int(number)
        frac_number = round(number - int_number, 1)
    else:
        raise ValueError('Wrong summa')

    nominal = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    current_summa = int_number
    i = 0
    while i < len(nominal)-1:
        division = current_summa//nominal[i]
        if division > 0:
            money_dict[nominal[i]] = division
            current_summa = current_summa - division*nominal[i]
        i+=1

    if frac_number > 0:
        i1 = frac_number // 0.5
        if i1 > 0:
            penny_dict[50] = int(i1)
        zi1 = frac_number - 0.5*i1
        i2 = round(zi1 / 0.1, 1)
        if i2 > 0:
            penny_dict[10] = int(i2)

    if money_dict and penny_dict:
        return money_dict, penny_dict
    elif money_dict:
        return money_dict
    else:
        return penny_dict

# print(summa_in_money(277538.56))
# print(summa_in_money(0.56))
# print(summa_in_money(277538))
