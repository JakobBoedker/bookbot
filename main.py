def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    words = book.split()
    return len(words)


def count_characters(book):
    words = str(book.split())
    lowerwords = words.lower()
    chardict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for char in lowerwords:
        if char in chardict:
            updateValue = chardict.get(char)
            chardict.update({char: updateValue+1})
    return chardict



def sort_on(d):
    return d["num"]





def book_report(book):
    mylist = []
    for char in book:
        mylist.append({"char": char, "num": book[char]})
    mylist.sort(reverse=True, key=sort_on)
    return mylist

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_report(count_characters(text))
    print("beginning of the report")
    print(f"Analyzing the book {book_path}")
    print(f"The book has {count_words(text)} words")
    for char in book_report(count_characters(text)):
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("end of the report")


if __name__ == "__main__":
    main()
