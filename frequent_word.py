def count_words(text):
    # Remove punctuation and convert to lowercase
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace("'", "")

    # Split the text into words
    words = text.split()

    # Count the frequency of each word using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    #print(word_counts)

    # Sort the words by frequency
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    #sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=False)

    # Display the top 5 most frequent words
    print("Top 5 most frequent words:")
    for word, count in sorted_word_counts[:5]:
        print(f"{word}: {count}")


text = input("Enter a string: ")
count_words(text)
