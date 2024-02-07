fileName = input("Enter the file to check: ").strip()
infile = open(fileName, "r")
vowels = set("A E I O U a e i o u")
text = infile.read().split()
countV = 0
for V in text:
    if V in vowels:
        countV += 1

