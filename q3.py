def vowelsCount():
    file = open('data.txt')
    content = file.read()
    vowels = list("AEIOUaeiou")
    count = 0
    for vowel in content:
        if vowel in vowels: count += 1
    return count
    print("Total vowels in file are:",vowelsCount() )