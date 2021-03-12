def checkDriverAge(driverage=0, accuracy=1):
    age = driverage

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        if accuracy > 0:
            print("Powering On. Enjoy the ride!")
        else:
            print('Be careful on the road!!!')
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(accuracy=-1,
               driverage=50)  # positional parameters. When you specify parameters in different order you need to specify their same names from function declaration in function call
checkDriverAge()  # if you want to invoke default parameter then simple omit it while calling the function
