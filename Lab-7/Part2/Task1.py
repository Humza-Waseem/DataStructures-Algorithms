def reverse_words(sentence):
    stack = []
    temp_word = ""

    # Step 2: Traverse the sentence character by character
    for char in sentence:
        # Step 3: Build temporary word until a space is encountered
        if char != ' ':
            temp_word += char
        else:
            # Step 4: Push the temporary word onto the stack
            stack.append(temp_word)
            temp_word = ""

    # Handle the last word in the sentence
    stack.append(temp_word)

    reversed_sentence = ""

    # Step 6: Pop elements from the stack to construct the reversed sentence
    while stack:
        reversed_sentence += stack.pop() + ' '

    return reversed_sentence.strip()


# Example usage
input_sentence = "I am from University of Engineering and Technology Lahore"
output_sentence = reverse_words(input_sentence)

print(output_sentence)
