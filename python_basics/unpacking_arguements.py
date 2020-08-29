# Way to collecting number of arguements 

def multiply(*args):
    print(args)
    total = 1
    for arg in args : 
        total = total * arg 
        
    return total

print(multiply(1, 3, 5))

print ("========================================================")
print ("========================================================")

def add (x,y): 
    return (x+y)

nums = [2, 5] 
print(add(nums))

print ("========================================================")
print ("========================================================")


