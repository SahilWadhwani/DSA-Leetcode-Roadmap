def words_to_number(s: str) -> int:
    s = s.lower()  # Normalize to lowercase
    words = s.strip().split()

    # Map number words to actual integers
    number_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90
    }

    # Multiplier words like hundred, thousand, million
    multiplier_map = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000
    }

    total = 0
    current = 0

    for word in words:
        if word in number_map:
            current += number_map[word]

        elif word == "hundred":
            current *= 100

        elif word in multiplier_map:
            current *= multiplier_map[word]
            total += current
            current = 0  # reset to process next chunk

        # Ignore "and" or unknown words gracefully
        else:
            continue

    return total + current
