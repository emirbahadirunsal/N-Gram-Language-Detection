import string # For string operations
import os # For file operations

n_values = [1, 2, 3] # n-gram sizes to consider
number_of_ngrams = 300 # Number of top n-grams to store

def find_ngrams(text, n, ngrams): # Find n-grams in text

    punctuation = string.punctuation.replace("'", "") # Exclude apostrophe from punctuation
    text = text.translate(str.maketrans("", "", punctuation)) # Remove punctuation characters from text
    text = text.lower() # Convert text to lowercase
    text = ''.join(char for char in text if not char.isdigit()) # Remove digits from text
    words = text.split() # Split text into words

    for word in words: # Iterate over words in text

        if n > 1:
            padded_word = "_" + word + "_" # Add padding underscores to word
        else:
            padded_word = word # Don't add padding underscores for unigrams

        for i in range(len(padded_word) - n + 1):
            ngram = padded_word[i:i + n] # Extract n-gram from padded word
            if ngram in ngrams:
                ngrams[ngram] += 1 # Increment n-gram count if it already exists
            else:
                ngrams[ngram] = 1 # Initialize n-gram count to 1 if it doesn't exist

folder_path = "exam_data" # Folder where the training files are stored
output_folder = "category_profiles" # Folder where the output files will be stored

languages = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))] # List of languages

for language in languages: # Iterate over languages

    ngrams = {} # Dictionary to store n-grams
    train_files = [f for f in os.listdir(os.path.join(folder_path, language)) if f.endswith("-ud-train.txt")] # List of training files

    for train_file in train_files: # Iterate over training files
        train_file_path = os.path.join(folder_path, language, train_file) # Training file path
        with open(train_file_path, "r", encoding="utf-8") as file: # Open training file
            train_text = file.read() # Read training file
            for n in n_values: # Iterate over n-gram sizes
                find_ngrams(train_text, n, ngrams) # Find n-grams in training file

    sorted_ngrams = sorted(ngrams.items(), key=lambda x: x[1], reverse=True) # Sort n-grams by count
    top_ngrams = dict(sorted_ngrams[:number_of_ngrams]) # Select top n-grams

    output_file = os.path.join(output_folder, f"{language}-train-outputs.txt") # Output file path
    with open(output_file, "w", encoding="utf-8") as output: # Open output file
        for ngram, count in top_ngrams.items(): # Iterate over top n-grams
            output.write(f"{ngram}\n") # Write n-gram to output file

    print(f"Top N-grams for {language} saved to {output_file}") # Print message to console