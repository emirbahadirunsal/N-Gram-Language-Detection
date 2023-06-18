# Language Detection using N-grams

This repository includes a language detection system that relies on the use of character N-grams. An N-gram is a contiguous sequence of N items from a given sample of text or speech. In this case, we consider N-grams of characters in a word, where N can be 1 (unigrams), 2 (bigrams), or 3 (trigrams).

## Scripts

There are two Python scripts in this repository: `train.py` and `test.py`.

- `train.py`: This script is responsible for training the language detection system. It takes as input a set of language files (in the folder named "exam_data"), creates N-grams from each file and saves the most frequent N-grams in an output file (in the folder named "category_profiles").
- `test.py`: This script is responsible for testing the language detection system. It takes as input a test file (named "test.txt"), creates N-grams from this file, and compares these with the N-grams from each language file to find the closest match.

## How to Use

Here is a step by step guide to use these scripts:

1. **Prepare your data**: Arrange your training data in the "exam_data" folder. The data should be structured such that each language has its own folder and within that folder, there should be one or more text files.

2. **Run the `train.py` script**: This will process all the text files in the "exam_data" folder and create language profiles for each language. These profiles will be saved in the "category_profiles" folder.

3. **Prepare your test file**: Create a text file named "test.txt" which contains the text whose language you want to predict.

4. **Run the `test.py` script**: This will process the "test.txt" file and compare its language profile with the profiles generated in the training step. It will output the name of the closest language as well as the calculated similarity probabilities for all languages.

## Dependencies

This project has been developed using Python 3 and doesn't require any additional libraries. The only requirement is that your data is text-based and is arranged as per the structure mentioned above.

## Future Work

This is a simple language detection system and may not work perfectly for languages with similar alphabets or sentence structures. Future work could look at using larger N-grams, or considering other features of the text such as common words or phrases.