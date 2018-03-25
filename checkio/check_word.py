def count_words(srinng1,tupple1):
    srinng1=srinng1.lower()
    count_word=0
    for word in tupple1:
        if (word in srinng1):
            count_word=count_word+1
    print  count_word
    return count_word

# count_words()
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"})