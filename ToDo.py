action = raw_input("What are you doing?")
day = raw_input("What day?").capitalize()

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
    action = raw_input("What are you doing?")
    day = raw_input("What day?").capitalize()
    while action != 'nothing':
        days_of_week[day].append(action)
    print days_of_week

add()


#
# def get(day):
#     print days_of_week[day]
#
# def choice():
#     user_choice = raw_input("What do you need?")
#     if user_choice == 'get':
#         print day
#         def()
