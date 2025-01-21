import random

def main():
    print("Keep it logically awesome.")

    with open("quotes.txt", "r") as f:
        quotes = f.readlines()

    random_quote = random.choice(quotes)
    print(random_quote.strip())

if __name__ == "__main__":
    main()