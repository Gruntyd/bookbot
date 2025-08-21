import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import get_num_words, get_char_use, chars_dict_to_list

def get_book_text(filepath):
	with open(filepath)as f:
		file_contents = f.read()
	return file_contents

def main():
	text = get_book_text(sys.argv[1])
	count = get_num_words(text)
	char_count = get_char_use(text)
	# print(char_count)
	sorted_char_list = chars_dict_to_list(char_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for entry in sorted_char_list:
		char_value = entry["char"]
		num_value = entry["num"]
		if char_value.isalpha():
			print(f"{char_value}: {num_value}")
	print("============= END ===============")

main()
