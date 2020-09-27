#Rennie Bevineau

#Create a garage for the cars
garage = []

#add 5 cars to the garage with this input loop that appends to the garage list
for i in range(0,5):
    newCar = input("car " + str(i+1) + "'s name? ")
    garage.append(newCar)


#store the car that the user wants to retrieve
car = input("Which car do you want to retrieve?")

#count the number of cars that are taken of the stack in order to find the car the user is looking for
count = 0
while garage.pop() != car:
    count += 1

#find the estimated time to retrieve the users vehicle and message it to the user
estimate = (count+1) * 5
print("Your estimated time to retrieve the vehicle is " + str(estimate) + " minutes")
