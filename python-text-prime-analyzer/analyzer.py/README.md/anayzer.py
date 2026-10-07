def count_words(sentence):
    """Return the number of words in a sentence."""
    return len(sentence.split())


def find_longest_word(sentence):
    """Return the longest word in a sentence."""
    words = sentence.split()

    if not words:
        return ""

    return max(words, key=len)


def reverse_sentence(sentence):
    """Return the sentence in reverse order."""
    return sentence[::-1]


def is_prime(number):
    """Return True if the number is prime, otherwise False."""
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    print("=== Text & Prime Analyzer ===")

    sentence = input("Enter a sentence: ")
    number = int(input("Enter a number: "))

    word_count = count_words(sentence)
    longest_word = find_longest_word(sentence)
    reversed_sentence = reverse_sentence(sentence)
    prime_result = is_prime(number)

    print("\n--- Results ---")
    print(f"Word Count       : {word_count}")
    print(f"Longest Word     : {longest_word}")
    print(f"Reversed Sentence: {reversed_sentence}")

    if prime_result:
        print(f"Prime Check      : {number} is a prime number.")
    else:
        print(f"Prime Check      : {number} is not a prime number.")


if __name__ == "__main__":
    main()