days_of_week = {
    'Monday': [] ,
    'Tuesday': [] ,
    'Wednesday': [] ,
    'Thursday' : [],
    'Friday' : [] ,
    'Saturday' : [] ,
    'Sunday' : []
}


def add():
    action = ""
    while action != 'nothing':
        action = raw_input("What are you doing?")
        if action == 'nothing':
            return None #replace with menu that refers back to first function
        day = raw_input("What day?").capitalize()
        days_of_week[day].append(action)
        print days_of_week


def get(day):
    print days_of_week[day]

def choice():
    user_choice = raw_input("What do you need?")
    if user_choice == 'get':
        day = raw_input("What day?").capitalize()
        get(day)
    if user_choice == 'add':
        add()

choice()
