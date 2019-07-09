import datetime
class User:
    pass

user1 = User()
user1.firstName = 'Larry'
user1.lastName = 'Bird'

print(user1.firstName, user1.lastName)

user2 = User()
user1.firstName = 'Magic'
user1.lastName = 'Johnson'



class Newuser:
    """
    hello, this is just some normal documentation

    """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        # extract first and last name
        name_pieces = full_name.split()
        # first_name = name_pieces[0]
        # last_name = name_pieces[1]
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]
    def age(self):
        """
        returns the age of the user based on their birthday
        """
        today = datetime.date.today()
        yyyy = int(self.birthday[:4])
        mm = int(self.birthday[4:6])
        day = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, day)
        age_in_days = (today - dob).days
        age_in_year = age_in_days / 365
        return int(age_in_year)

user = Newuser('Ahmed Sherif', '19771231')
print(user.name)
print(user.birthday)
print(user.first_name)
print(user.last_name)
print(user.age())
# help(Newuser)