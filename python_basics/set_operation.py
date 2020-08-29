friends = {"vipin", "nikhil", "anurag"}
abroad = {"vipin", "anurag"}

## difference 
local = friends.difference(abroad)
print(local)
## local = {"nikhil"}

total = local.union(abroad); 
print(total)


