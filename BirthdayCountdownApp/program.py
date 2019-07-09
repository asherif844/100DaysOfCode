import datetime

def print_header():
    print('--------------------')
    print('     Birthday App   ')
    print('--------------------')
    print()


def get_birthday_from_user():
    while True:
        try:
            print('When were you born?')
            year = int(input('Year [YYYY]'))
            month = int(input('Month [MM]'))
            day = int(input('Day [DD]'))
            birthday = datetime.date(year, month, day)
            return birthday
        except ValueError:
            print('This is not a number, please enter your date credentials again!')
            continue
        else:
            break


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year-target_date 
    return dt.days

def print_birthday_information(days):
    if days<0:
        print('You had your birthday {} days ago'.format(abs(days))) 
    elif days>0:
        print('Your birthday is in {} days'.format(days))
    else:
        print('Your birthday is today! Yay!')

def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.date.today()
    
    number_of_days = compute_days_between_dates(bday, now)
    # print(number_of_days)
    print_birthday_information(number_of_days)

main()
