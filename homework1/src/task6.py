#Task6.py

# Function to count all words in file
def count_Words(filename):
    # When we open we first read all contents and split by space and return the length
    with open (filename,"r") as file:
        return len(file.read().split())
