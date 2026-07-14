from wordfreq import top_n_list
words = top_n_list("en", 50000000000000)
five_letter_words = [
    w.lower()
    for w in words
    if len(w) == 5 and w.isalpha()
]