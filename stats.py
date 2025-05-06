def main(path_to_file):
	words = get_num_words(path_to_file)
	chars = get_num_characters(path_to_file)
	
	print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_file}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")
	for item in chars:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		text = f.read()
	return text

def get_num_words(path_to_file):
	with open(path_to_file) as f:
		text = f.read()
		words = text.split()
		count = len(words)
	return count

def get_num_characters(path_to_file):
	with open(path_to_file) as f:
		char_counts = {}
		text = f.read()
		text = text.lower()
		for char in text:
			char_counts[char] = char_counts.get(char, 0) + 1
		final_count = sorted_char_counts(char_counts)
		filtered = [item for item in final_count if item["char"].isalpha()]
	return filtered

def sorted_char_counts(char_counts):
	sort_counts = [{"char": key, "num": value} for key, value in char_counts.items()]
	sort_counts.sort(reverse=True, key=sort_on)
	return sort_counts

def sort_on(dict):
	return dict["num"]
