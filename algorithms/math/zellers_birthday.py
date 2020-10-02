import argparse
"""Zellers Congruence Birthday Algorithm
    Find out what day of the week you were born on
    Accepts birthday as a string in mm-dd-yyyy format 
"""

def zeller(bday):

    days = {
        '0': 'Sunday',
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Saturday'
    }

    m = int(bday[0] + bday[1])
    d = int(bday[3] + bday[4])
    y = int(bday[6] + bday[7] + bday[8] + bday[9])

    if m <= 2:
        y = y - 1
        m = m + 12
    c = int(str(y)[:2])
    k = int(str(y)[2:])

    t = int(2.6*m - 5.39)
    u = int(c / 4)
    v = int(k / 4)
    x = d + k
    z = t + u + v + x
    w = z - (2 * c)

    f = round(w%7)

    for i in days:
        if f == int(i):
            print("Your birthday " + bday + ", was a " + days[i] + "!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find out what day of the week you were born on Accepts birthday as a string in mm-dd-yyyy or mm/dd/yyyy format')
    parser.add_argument('bday', type=str, help='Date as a string (mm-dd-yyyy or mm/dd/yyyy)')
    args = parser.parse_args()
    zeller(args.bday)