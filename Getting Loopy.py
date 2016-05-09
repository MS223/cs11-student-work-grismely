print "hello"[1:] #removes the first letter of the string
print "hello"[:4] #removes the last letter of string
print "hello"[2:4] #possibly removes second and last letter?




def fruit_pluralizer(fruit):
    for n in fruit:
        if n[:len(n)]== 'y':
            print n[:len(n)-1] + 'ies'
        else:
            print n[:len(n)] + 's'

fruit =['apple','berry','banana','cherry']

fruit_pluralizer(fruit)
