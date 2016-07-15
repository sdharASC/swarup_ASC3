print("List Lab Problems")
print("")

one = range(10, 21)
print("#1: ", one)
#---------------------

two = []
for i in range(5):
    two.append(0)
print("#2: ", two)
#---------------------

three = []
print("#3: ", three)
#---------------------

print("#4:  Skipped (covered in 2)")
#---------------------

five = ["a", 5, "doodle", 3, 10]
print("#5: ", len(five))
#---------------------

six = ["a", 5, "doodle", 3, 10]
del(six[2])
print("#6: ", six)
#---------------------

seven = ["a", 5, "doodle", 3, 10]
seven.append("Another element")
print("#7: ", seven)
#---------------------

eight = ["a", 5, "doodle", 3, 10]
eight[0] = 8.4
print("#8: ", eight)
#---------------------

nine = ["a", 5, "doodle", 3, 10]
nine.insert(0, "New Element")
print("#9: ", nine)
#---------------------

ten = []
for i in range(10):
    if i % 2 == 1:
        ten.append(i)
print("#10:", ten)

