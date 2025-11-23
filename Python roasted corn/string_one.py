list = ["book","salt","mom", "target"]
for word in list:
    sliced_word = ""
    sliced_word = (word[::len(word)-1])
    if sliced_word[0] == sliced_word[1]:
        print(word)