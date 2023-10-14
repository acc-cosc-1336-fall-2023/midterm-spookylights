import question_c

def calculate_bonus_pay():
    sales = int(input("Please enter the sales amount: "))

    bonus = question_c.get_bonus_pay(sales)
    if bonus == "Invalid Arguments":
        print(bonus)
    else:
        format_bonus = "{:.2f}".format(bonus)
        print("Your calculated bonus is: ", format_bonus)

calculate_bonus_pay()