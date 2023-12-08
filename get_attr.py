class emp:
    name ="empty"
    city ="empty"
emp1 =emp()
emp1.name = "zino"
emp1.city = "algiers"

print(getattr(emp1 ,"name"))
print(getattr(emp1 ,"city" ))
