value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue # continue skips the 5 on the condition, but resumes the loop +1
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# A for loop iterates over a sequence of a collection of datatypes

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara": # once more, continue stops the current iteration, 
#         continue    # and goes into the next iteration in the loop
#     print(x)

for x in range(2, 4): # range includes initial number, but not the last number
    print(x) # so if you want to include 100 as the end of the range, make it instead >101

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names: # outer loop iterates +1 once it's done with the inner loops
        print(name + " " + action + ".")