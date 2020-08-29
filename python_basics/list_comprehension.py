numbers = [1, 3, 5] 
doubled = []

for num in numbers : 
    doubled.append(num * 2)

print (doubled)

print ("================================================================")
print ("================================================================")
print ("================================================================")


doubled = [num * 2 for num in numbers]  ## list comprehension
print (doubled)
print ("================================================================")
print ("================================================================")
print ("================================================================")

friends = ["sam", "sourabh", "abhi", "shakti", "dinesh", "kailash"]
start_s = [friend for friend  in friends if friend.startswith("s")]
print(start_s)
