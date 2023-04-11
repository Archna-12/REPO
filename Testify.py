import os

def create_index(book_path, exclude_words_path, index_path):
    # Read the book text
    with open(book_path, 'r') as book_file:
        book_text = book_file.read()

    # Read the exclude words
    with open(exclude_words_path, 'r') as exclude_words_file:
        exclude_words = exclude_words_file.read().split()

    # Split the book text into words
    words = book_text.split()

    # Remove excluded words and convert words to lowercase
    words = [word.lower() for word in words if word.lower() not in exclude_words]

    # Create a dictionary to store the word index
    word_index = {}

    # Loop through the words and populate the word index
    for i, word in enumerate(words):
        if word not in word_index:
            word_index[word] = []
        word_index[word].append(i + 1)  # Adding 1 to the index to make it 1-based instead of 0-based

    # Write the word index to the index file
    with open(index_path, 'w') as index_file:
        for word, indexes in word_index.items():
            index_file.write(f"{word}: {', '.join(map(str, indexes))}\n")

    print(f"Word index created successfully and saved to {index_path}.")


# Paths to the data files
book_path = "Assignment.txt"
exclude_words_path = "exclude-words.txt"
index_path = "index.txt"

# Call the function to create the word index
create_index(book_path, exclude_words_path, index_path)
