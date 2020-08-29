def hello():
    print ("Hello") 

hello()

print ("=======================================")
print ("=======================================")

def user_age_in_sec():
    user_age = int(input("Enter your age : "))
    age_in_sec = user_age * 365 * 24 * 60 * 60 
    print (f"your age in sec is {age_in_sec} ")

user_age_in_sec()
