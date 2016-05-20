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

# days_of_week[day].append(action)
# print days_of_week

def update():
    while action != 'nothing':
        action = raw_input("What are you doing?")
        day = raw_input("What day?").capitalize()

days_of_week[day].append(action)
#
#     #shuld get our action variable and add it yo our dictionary days_of_week with the key day
#
# days[day] = action
# print days_of_week
