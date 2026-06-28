def count_vowels(text):

    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count += 1

    return count

word = input("Enter a word: ")

print("Number of vowels =", count_vowels(word))