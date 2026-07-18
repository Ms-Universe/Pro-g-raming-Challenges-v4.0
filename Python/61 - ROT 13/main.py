alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def rot13(phrase: str) -> str:
    global alphabet
    out = ""
    for char in phrase:
        if char in alphabet:
            out += alphabet[(alphabet.index(char) + 13) % len(alphabet)]
        else:
            out += char
    return out


# Calls rot13 on the given phrase until it is back to its original form
def rot13_cycle(phrase: str):
    current_phrase = phrase
    for i in range(len(alphabet) // 13):
        current_phrase = rot13(current_phrase)
        print("Iteration " + str(i) + ": " + current_phrase)


def main():
    phrase = input("Enter a phrase\n>| ")
    rot13_cycle(phrase)


if __name__ == "__main__":
    main()
