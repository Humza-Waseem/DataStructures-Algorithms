def reversedWords(sentence):
    stack = []
    tempWord = ""

     
    for i in range(0,len(sentence) ):
        if(sentence[i] != ' '):
            tempWord = tempWord + sentence[i]
        else:
            stack.append(tempWord)
            tempWord = ""

    stack.append(tempWord)

    reversedSentence = ""

    while stack:
        reversedSentence += stack.pop() + ' '

    return reversedSentence  


sentence = "I am from University of Engineering and Technology Lahore" # we pop from Lahore to I   
          # 9<-8 <-7    <-6      <-5   <-4      <-3   <- 2   <-   1
output_sentence = reversedWords(sentence)

print(output_sentence)


