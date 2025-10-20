def count_total_words(text):
    words = text.split()
    
    return len(words)

def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_by_count(chars):
    return chars["num"]

def format_char_counts(count):
    list = []

    for char in count:
        list.append({"char": char, "num": count[char]})

    list.sort(reverse=True, key=sort_by_count)

    return list