letters = ['D','E','E','L','T']

all_words = []

def get_all_words(letters):
    if len(letters) == 1:
        return letters
    else:
        for i in range(len(letters)):
            