my_list = ["abc", "aba", "uvwxyz", "1221"]
my_2nd_list = ["efg", "1221", "jklm", "qrs"]

def common_words(my_list, my_2nd_list):
    result = []
    true = ""
    for i in my_list:
        if i in my_2nd_list:
            result.append(i)
            true = "True."
    return true

print(common_words(my_list, my_2nd_list))