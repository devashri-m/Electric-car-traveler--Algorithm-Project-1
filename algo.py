#
# This Code is Submitted by Team Titans
# Team Members: Sumit Bishnoi, Apoorva Machale, Devashri Manepatil
#
# We start our code by taking input from users
while True:
    c = int(input("Enter the Total miles :"))  # C represents Capacity/Total charge
    if 250 <= c <= 300:
        break
    else:
        print("Enter correct value for total miles it should be between 250 and 300 miles!!\n")

while True:
    n = int(input("Enter the number of cities :"))  # n represents the total number of cities that we will visit
    if 3 < n < 20:
        break
    else:
        print("Enter correct value for cities it should be between 3 and 20!!!\n")

#  Creating an empty list which will helps us to records city where we charge our car
result = []
if n >= 0:
    result.append(chr(65))

#  Creating a dictionary which will saves all the records as keys(cities) and values(Distance between cities)
Citydict = {}

# Here we are using ASCII values to convert input variable n to cities name
for i in range(65, 65 + n):
    if i == 65 + n - 1:
        Citydict[chr(i)] = 0
    else:
        #  Here we are storing cities and distance(That is taken from users) as keys and values in dictionary
        while True:
            d = int(input("Enter Distance between " + chr(i) + " and " + chr(i + 1) + ":"))
            if 10 < d < c // 2:
                break
            else:
                print("Enter correct value for distance between cities it should be between 10 and " + str(
                    c // 2) + "!!!\n")
        Citydict[chr(i)] = d

# Uncomment the line below to see the stored data in the dictionary
# print(Citydict)

# Here we are temporary storing value of total capacity
temp = c

print("---------------------------------------------------")
print("Let's Start our travel!!")
print("---------------------------------------------------")

# Here we are using for loop to iterate through our dictionary
for keys, value in Citydict.items():
    print("Charge Capacity Left :", c)
    print("Current City :", keys)

    # Car will only go to next city when distance between 2 cities is greater than car charge capacity
    if c >= 2 * value:
        c = c - value
    else:
        # Here we are charging the car depending upon distance between cities and final destination
        result.append(keys)
        # When the capacity is less than 100 miles, we charge the car to its maximum capacity.
        if c < 100:
            c = temp
            print("-------------------------------------------")
            print("Charging car to full capacity at city:", keys)
            print("-------------------------------------------")
        # Here we are charging when the total of capacity and distance (between present city and next city)
        # is greater than twice the distance.
        elif c + value > 2 * value:
            c = c + value
            print("-------------------------------------")
            print("Charging car partially at city:", keys)
            print("-------------------------------------")
        # Here we are charging when the total of capacity and distance (between present city and next city)
        # is less than twice the distance.
        elif c + value < 2 * value:
            c = c + 2 * value
            print("--------------------------------------")
            print("Charging car partially at city:", keys)
            print("--------------------------------------")
if n >= 1:
    result.append(chr(65 + n - 1))
print("-----------------------------------------------------------")
print("Cities where we stopped to charge our car :", result)

# Enjoy!!
