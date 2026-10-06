import string

def count_unique_words(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    
    words = clean_text.split()
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

sample_text = "hello."

word_dict = count_unique_words(sample_text)
print(word_dict)

frequent_words = [word for word, count in word_dict.items() if count > 3]
print(frequent_words)
