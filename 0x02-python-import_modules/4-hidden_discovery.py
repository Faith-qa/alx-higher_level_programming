#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for word in dir(hidden_4):
        if word[1] != '_':
            print(word)
