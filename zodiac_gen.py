# did a project similar to this when i attended an ID tech camp at umd a few years ago and just wanted to try remaking it now
#   - take user input for birth month and birthday 
#   - send output message of their zodiac 

# zodiacs and their dates
zodiacs = [
    {
        "name": "aquarius",
        "start": (1, 20),
        "end": (2, 18)
    },
    {
        "name": "pisces",
        "start": (2, 19),
        "end": (3, 20)
    },
    {
        "name": "aries",
        "start": (3, 21),
        "end": (4, 19)
    },
    {
        "name": "taurus",
        "start": (4, 20),
        "end": (5, 20)
    },
    {
        "name": "gemini",
        "start": (5, 21),
        "end": (6, 21)
    },
    {
        "name": "cancer",
        "start": (6, 22),
        "end": (7, 22)
    },
    {
        "name": "leo",
        "start": (7, 23),
        "end": (8, 22)
    },
    {
        "name": "virgo",
        "start": (8, 23),
        "end": (9, 22)
    },
    {
        "name": "libra",
        "start": (9, 23),
        "end": (10, 23)
    },
    {
        "name": "scorpio",
        "start": (10, 24),
        "end": (11, 21)
    },
    {
        "name": "sagittarius",
        "start": (11, 22),
        "end": (12, 21)
    },
    {
        "name": "capricorn",
        "start": (12, 22),
        "end": (1, 19)
    }
]

# convert month names to numbers
month_names = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

def get_zodiac(month, day):
    for sign in zodiacs:
        start_month, start_day = sign["start"]
        end_month, end_day = sign["end"]
            
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign["name"]
        
    return "invalid"

while True:  
    # month input
    month_input = input("what month were you born? ").lower()

    # check if they input a number or name
    if month_input.isdigit():
        month = int(month_input)
    else:
        month = month_names.get(month_input)

    # validate + continue 
    if month is None or not 1 <= month <= 12:
        print("invalid.")
        continue
    else:
        day = int(input("what day were you born? "))
        zodiac_sign = get_zodiac(month, day)
        print(f"you are a {zodiac_sign}!")
    
    again = input("do you want to check another birthday? (yes/no) ")
    if again != "yes":
        print("okay! bye bye!")
        break
    
    
# # beginner code 
# if month == 1 and day <= 20 or month == 2 and day <= 18:
#     print("you are an aqaurius!")
# elif month == 2 and day <= 19 or month == 3 and day <= 20:
#     print("you are a pisces!")
# elif month == 3 and day <= 21 or month == 4 and day <= 19:
#     print("you are an aries!")
# elif month == 4 and day <= 20 or month == 5 and day <= 20:
#     print("you are a taurus!")
# elif month == 5 and day <= 21 or month == 6 and day <= 21:
#     print("you are a gemini!")
# elif month == 6 and day <= 22 or month == 7 and day <= 22:
#     print("you are a cancer!")
# elif month == 7 and day <= 23 or month == 8 and day <= 22:
#     print("you are a leo!")
# elif month == 8 and day <= 23 or month == 9 and day <= 22:
#     print("you are a virgo!")
# elif month == 9 and day <= 23 or month == 10 and day <= 23:
#     print("you are a libra!")
# elif month == 10 and day <= 24 or month == 11 and day <= 21:
#     print("you are a scorpio!")
# elif month == 11 and day <= 22 or month == 12 and day <= 21:
#     print("you are a sagittarius!")
# elif month == 12 and day <= 22 or month == 1 and day <= 19:
#     print("you are a capricorn!")
# else:
#     print("invalid")
