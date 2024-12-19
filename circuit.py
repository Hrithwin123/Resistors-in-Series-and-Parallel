rows = int(input("Enter the number of rows in the circuit : "))
print("\n")
resistances = []

sum = []

def circuitPrinter(resistances):
    rowlist = []
    resrow = ["-----"]
    max = 0
    for row in resistances:
        if(len(row)> max):
            max = len(row)
    max = (max*5) + max * 6 + 5
    
    
    c = len(resistances)

    for row in resistances:
        for resistor in row:
            single = f"[{resistor} Ω]".ljust(10, "-")
            resrow.append(single)
        if(c<=1):
            resrow.append("|" + " ")
        else:
            resrow.append("|"+"\n")
            c-=1

        rowlist.append("|"+"".join(resrow).rjust(max, "-").ljust(max, "-"))
        resrow = ["-----"]

    print("".join(rowlist))
    print("|" + ((max - 2) * " ") + "|")
    

for i in range(rows):
    r = []
    num = int(input(f"Enter the number of resistors in row {i+1} : "))
    for i in range(num):
        res = int(input(f"Enter the resistance of {i+1} resistor : "))
        r.append(res)
    resistances.append(r)
    print("\n")
    

circuitPrinter(resistances)

for row in resistances:
    s = 0
    for resistor in row:
        s+= resistor
    sum.append(s)

parmul = 1
parsum = 0
for i in sum:
    parmul *= i
    parsum += i
print("\n")
print(f"The equivalent resistance is %0.2f Ω" %(parmul/parsum))







