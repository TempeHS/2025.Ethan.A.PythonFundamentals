names = []

with open("Names.txt"):
    for line in file:
        names.append(line.rstrip())
# sorts the names from A-Z reverse=True can be used for Z-A
for name in sorted(names):
    print(f"hello, {name}")

# names.csv (Comma-Seperated values) stores multiple pieces of information that are related in the same file
