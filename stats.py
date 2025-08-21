def get_num_words(text):
        words = text.split()
        return len(words)

def get_char_use(book): # Gets the count for each character within a book
	char_counts = {}
	for char in book:
		lowered_char = char.lower()
		if lowered_char not in char_counts:
			char_counts[lowered_char] = 1
		else: char_counts[lowered_char] += 1
	return char_counts

def sort_on(items):
	return items["num"]

def chars_dict_to_list(char_counts_dict):
	sorted_list = []
	for key, value in char_counts_dict.items():
		sorted_list.append({"char": key, "num": value})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list


