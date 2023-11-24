from sys import exit
names = []

while True:
    try:
        name = input(" ")
    except EOFError:
        break
    if name == 'd':
        break
    names.append(name)

length = len(names)

if length == 1:
    print("Adieu, adieu, to", names[0])
elif length == 2:
    print("Adieu, adieu, to", names[0], "and", names[1])
elif length == 3:
    print("Adieu, adieu, to", names[0] + ",", names[1] + ",", "and", names[2])
else:
    output = "Adieu, adieu, to"
    for i in range(length - 1):
        output += " " + names[i] + ","
    output += " and " + names[length - 1]
    print(output)

exit(0)