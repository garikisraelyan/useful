# {"x": [11, 12, 13, 14, 15, 16, 17, 18, 19]
# "y": [21, 22, 23, 24, 25, 26, 27, 28, 29]
# "z": [31, 32, 33, 34, 35, 36, 37, 38, 39]
# }

my_dict = {"x": [],
"y": [],
"z": []
}

# for i in range(11, 20):
#     my_dict["x"].append(i)

# for j in range(21, 30):
#     my_dict["y"].append(j)

# for k in range(31, 40):
#     my_dict["z"].append(k)

# print(my_dict)
# dict_keys = my_dict.keys()

# for l in dict_keys:
#     a = my_dict[l][4]
#     print(a)

# my_dict["x"] = list(range(11, 20))
# my_dict["y"] = list(range(21, 30))
# my_dict["z"] = list(range(31, 40))

while True:
    try:
        user_input = input("Enter a range which contains 9 elements: ")

        a = 0
        if "_" in user_input:
            a = user_input.index("_")

        first_element = int(user_input[:a])
        second_element = int(user_input[a+1:])

        if second_element - first_element == 8:
            x_list = list(range(first_element, second_element+1))
            my_dict.update({"x": x_list})
            print(my_dict)
            break
        else:
            print("Your range is invalid.")
    except:
        print("Your range is invalid.")
