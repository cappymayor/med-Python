from datetime import datetime
def current_age(birth_year:"int"):

    current_year = datetime.now().year
    return current_year - birth_year

print(current_age(1990))
print(current_age(1999))

def count_string(string:"str"):
    return len(string)

print(count_string("coconut"))
print(count_string("Welcome to a beautiful country filled with wonderful people, amazing cultures, exciting opportunities, rich history, delicious food, breathtaking landscapes, and countless places to explore and enjoy. We hope your stay is enjoyable, memorable, peaceful, and full of amazing experiences!"))
print(count_string("ffjfkjfbnjfbfijfijjfbfjknfjfkofjkfijvihivgyuyfgfhfwuihfwijfwbijf"))


def welcome_message(name:"str",country:"str"):
   
    return f"Welcome {name} from {country}!"
print(welcome_message("John", "USA"))


def largest_number(*numbers):
    return max(numbers)

print(largest_number(12,34,56,7,6,79,80,20,16,12,30,45,488,100,200,300,400,500,600,700,800,900,1000))

def person_voting(person_age:"int"):
    if person_age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

print(person_voting(20))
print(person_voting(16))