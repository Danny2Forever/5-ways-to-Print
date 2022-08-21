weight = int(input("Enter weight : "))
height = int(input("Enter height : "))

print(str(weight) + " " + str(height))
print("%s %s" % (weight, height))
print("{} {}". format(weight, height))
print(f"{weight} {height}")
print("%(w)s %(h)s" % {'w': weight, 'h': height})
