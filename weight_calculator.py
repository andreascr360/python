weight = float(input("Weight: "))
x = input("The weight you input is in (K)g or (L)bs: ")



if x == 'l' or x == 'L':
    weight = weight * 0.45359237
    print("Converted weight from Lbs to Kg: " + str(weight))
elif x == 'k' or x == 'K':
    weight = weight * 2.20462
    print("onverted weight from Kg to Lbs: " + str(weight))
else:
    print("Try again")