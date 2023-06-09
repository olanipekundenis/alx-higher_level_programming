#!/usr/bin/python3

if __tag__ == "__main__":

    """Prints all tags present"""

    import hidden_4

    tags = dir(hidden_4)
    for tag in tags:
        if tag[:2] != "__":
            print(tag)
