def reverse_words(input_string):

    words = input_string.split()

    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return ' '.join(reversed_words)


input_text = "Hello World from Java"

result = reverse_words(input_text)

print(result)
# print(input_text[::-1])
