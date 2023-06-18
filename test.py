import string # For string operations
import os # For file operations

n_values = [1, 2, 3]  # n-gram sizes to consider
number_of_ngrams = 300  # Number of top n-grams to store
max = 300  # Maximum distance for a position comparison
max_distance = number_of_ngrams * max  # Maximum distance for a language comparison

def find_ngrams(text, n, ngrams): # Find n-grams in text

    punctuation = string.punctuation.replace("'", "")  # Exclude apostrophe from punctuation
    text = text.translate(str.maketrans("", "", punctuation))  # Remove punctuation characters from text
    text = text.lower()  # Convert text to lowercase
    text = ''.join(char for char in text if not char.isdigit())  # Remove digits from text
    words = text.split()  # Split text into words

    for word in words: # Iterate over words in text
        if n > 1:
            padded_word = "_" + word + "_"  # Add padding underscores to word
        else:
            padded_word = word # Don't add padding underscores for unigrams

        for i in range(len(padded_word) - n + 1): # Iterate over n-grams in the word
            ngram = padded_word[i:i + n] # Extract n-gram from padded word
            if ngram in ngrams:
                ngrams[ngram] += 1 # Increment n-gram count if it already exists
            else:
                ngrams[ngram] = 1 # Initialize n-gram count to 1 if it doesn't exist

def calculate_distance(ngrams1, ngrams2): # Calculate distance between two languages

    distance = 0

    for ngram, _ in ngrams1.items(): # Iterate over n-grams in test file
        if ngram in ngrams2: # Check if n-gram is present in train file
            pos1 = ngrams1[ngram] # Position of n-gram in test file
            pos2 = ngrams2[ngram] # Position of n-gram in train file
            position_diff = abs(pos1 - pos2) # Difference between positions
            distance += position_diff # Add difference to distance
        else:
            distance += max # Add maximum distance to distance

    return distance

def load_ngrams_from_file(file_path): # Load n-grams from file

    ngrams = {} # Dictionary to store n-grams

    with open(file_path, "r", encoding="utf-8") as file: # Open file
        for line_num, line in enumerate(file, start=1): # Iterate over lines in file
            ngram = line.strip() # Remove trailing newline character
            ngrams[ngram] = line_num # Add n-gram to dictionary

    return ngrams

def find_closest_language(test_file_path): # Find the closest language for the test file
    
    test_ngrams = {} # Dictionary to store n-grams in test file

    with open(test_file_path, "r", encoding="utf-8") as file: # Open test file
        test_text = file.read() # Read test file
        for n in n_values: # Iterate over n-gram sizes
            find_ngrams(test_text, n, test_ngrams) # Find n-grams in test file

        test_ngrams = sorted(test_ngrams.items(), key=lambda x: x[1], reverse=True) # Sort n-grams by count
        test_ngrams = [(ngram, i + 1) for i, (ngram, _) in enumerate(test_ngrams)] # Add position to n-grams
        test_ngrams = dict(test_ngrams[:number_of_ngrams]) # Store only top n-grams

    closest_language = None # Initialize closest language to None
    min_distance = float("inf") # Initialize minimum distance to infinity

    for language in languages: # Iterate over languages

        train_file_path = os.path.join(output_folder, f"{language}-train-outputs.txt") # Path to train file
        train_ngrams = load_ngrams_from_file(train_file_path) # Load n-grams from train file
        distance = calculate_distance(test_ngrams, train_ngrams) # Calculate distance between languages
        print(f"The probability for {language} is: {((max_distance - distance) / max_distance) * 100:.2f}%") # Print predicted accuracy

        if distance < min_distance: # Check if distance is less than minimum distance
            min_distance = distance # Update minimum distance
            closest_language = language # Update closest language

    if min_distance == 0 and not test_ngrams: # Check if minimum distance is 0 and test file is empty
        closest_language = "Not a proper language" # Update closest language

    return closest_language

folder_path = "exam_data" # Path to the folder containing the train files
output_folder = "category_profiles" # Path to the folder containing the train files

languages = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))] # List of languages
test_file = "test.txt" # Path to the test file
closest_language = find_closest_language(test_file) # Find the closest language for the test file

print(f"\nClosest Language: {closest_language}") # Print closest language