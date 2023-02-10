array_A = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

array_A = sorted([i for i in array_A if not str(i).isdigit()]) + sorted([i for i in array_A if str(i).isdigit()])

print(array_A)