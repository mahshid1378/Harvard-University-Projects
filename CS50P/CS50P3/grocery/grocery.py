from collections import defaultdict
from sys import exit

grocery_list = defaultdict(int)

while True:
    try:
        item = input("")
    except EOFError:
        break
    grocery_list[item.lower()] += 1

sorted_list = sorted(grocery_list.items(), key=lambda x: x[0])

output = "\n".join([f"{count} {item.upper()}" for item, count in sorted_list])
print(output)

exit(0)