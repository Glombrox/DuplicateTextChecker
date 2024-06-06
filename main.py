
text = input("Write a string of text and/or numbers and press enter:\n")

# Check if the input is empty
if len(text) == 0:
    print("There is no text!!!")
    exit(0)
# Convert string into lower case
text = text.lower()

# Split the string into words with " "
word = text.split(" ")

for i in range(0, len(text)):
    count = 1
    for j in range(i+1, len(word)):
        if word[i] == word[j]:
            count = count + 1
            # Set word[j] = "0" to avoid printing the same word twice
            word[j] = "0"

    # Display the duplicate word(s)
    if count > 1 and word[i] != "0":
        print("The duplicate text is :\n", word[i])
