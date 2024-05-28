weight = float(input("Peso: "))
value = input("(K)g ou (L)bs:")
if value.upper() == "K":
    convert = weight * 2.20
    print("Peso em Lbs: " + str(convert))
else:
    convert = weight / 2.20
    print("Peso em Kg: " + str(convert))
