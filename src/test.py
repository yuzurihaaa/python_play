from src.test_import import *

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
