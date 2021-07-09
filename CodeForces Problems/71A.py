n = int(input())
for i in range(n):

    word = input()
    original_length = len(word)
    length = len(word) - 2

    def if_long(word):
        long_word_list = list(word)
        print(long_word_list[0] + str(length) + long_word_list[-1])

    def if_not_long(word):
        print(word)

    if(original_length > 10):
        if_long(word)

    else:
        if_not_long(word)

#TODO Complete this question



