def get_bonus_pay(sales):
    if sales < 0:
        return "Invalid Arguments"
    elif sales in range(0, 500):
        bonus = sales * .05
        return bonus
    elif sales in range(500, 1000):
        bonus = sales * .06
        return bonus
    elif sales in range(1000, 1500):
        bonus = sales * .07
        return bonus
    elif sales in range(1500, 2000):
        bonus = sales * .08
        return bonus
    else:
        return "Invalid Arguments"