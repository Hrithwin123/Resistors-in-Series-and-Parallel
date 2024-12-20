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
    

def voltagePrinter(resistances, volt):
    max = 0
    for row in resistances:
        if(len(row)> max):
            max = len(row)
    max = (max*5) + max * 6 + 5
    circuitPrinter(resistances)
    print("|" + ((max - 2) * " ") + "|")
    print("|" + ((max - 2) * " ") + "|")
    print("|"+f"({volt})".rjust(int(max/2), "-").ljust(int(max-2), "-") +"|")
    print("\n")
    print("\n")


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
eqres = parmul/parsum
print(f"The equivalent resistance is %0.2f Ω" %(eqres))
print("\n")


print("Do you want to calculate Current or Potential Difference ?")
print("1) Current (c)")
print("2) Voltage (v)")
user = input()
user = user.lower()
if(user == "c" or user == "current" or user == "1"):
    volt = int(input("Enter the potenital difference (in volts) : "))
    current = volt / eqres
    voltagePrinter(resistances, volt)
    print("\n")
    print(f"The current flowing through the circuit is %0.2f A" %(current))

elif(user == "v" or user == "voltage" or user == "2"):
    current = int(input("Enter the current (in amperes) : "))
    volt = current * eqres
    voltagePrinter(resistances, int(volt))
    print(f"The potential difference across the circuit is %0.2f A" %(volt))
    print("\n")
else:
    print("please enter a valid input and try again")











