def handle_balance(balances):
    while balances > 0:
        print("Amount of balance you need to pay remaining : ", balances)
        payment_given = int(input("Please insert amount of payment : "))
        if payment_given < 0:
            print("Please enter a positive number")
        else:
            balances = balances - payment_given

    if balances < 0:
        print(" Your balance is : ", abs(balances))

    print("Thank you for your payment! ")


def check_user(user_status):
    if user_status == 'yes':
        return 'student'
    else:
        return 'public'


def check_week(day_input):
    if day_input in ['saturday', 'sunday']:
        return 'weekend'
    else:
        return 'weekday'


def check_sport_name(sport_names, games):
    if sport_names.lower() not in games.keys():
        return check_sport_name(input("Please select the court you would like to book by inserting game : "), games)
    else:
        print("You inserted number : %s" % sport_names)
        return sport_names