def reverse(text):

    if len(text) == 0:
        return text

    return reverse(text[1:]) + text[0]

word = input("Enter a word: ")

print("Reversed String:", reverse(word))