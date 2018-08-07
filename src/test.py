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


if __name__ == '__main__':
    games = {
        "futsal": {
            "student": {
                "weekend": 50,
                "weekday": 50
            },
            "public": {
                "weekend": 80,
                "weekday": 60
            }
        },
        "sepak takraw": {
            "student": {
                "weekend": 25,
                "weekday": 20
            },
            "public": {
                "weekend": 65,
                "weekday": 60
            }
        },
        "basketball": {
            "student": {
                "weekend": 55,
                "weekday": 55
            },
            "public": {
                "weekend": 85,
                "weekday": 65
            }
        },
        "badminton": {
            "student": {
                "weekend": 30,
                "weekday": 35
            },
            "public": {
                "weekend": 65,
                "weekday": 60
            }
        }
    }

    print("Welcome to Uniten Sports Complex Court Rental System")
    print("""
    List of Game
    Futsal
    Sepak Takraw
    Basketball
    Badminton
    """)

    sport_name = check_sport_name('', games)

    status = input("Are you a Uniten Student? (Type Yes or No) : ")

    while status.lower() not in ['yes', 'no']:
        status = input("Please enter only 'Yes' or 'No' : ")

    status = check_user(status)

    day = input("When would you like to book the court , mention the day only : ")

    week = check_week(day)

    print("You chose %s as option." % day)

    hour = int(input("How many hours would you like to book/rent the court(Kindly type numbers only):  "))

    payment_cost = games[sport_name.lower()][status][week]

    print(
        "Rental Details \n"
        "Game : %s \n"
        "Uniten Student or Public : %s \n"
        "Day : %s \nHours : %s \n"
        "Total amount you need "
        "to pay : %s" % (sport_name, status, day, hour, payment_cost))

    handle_balance(int(payment_cost))
