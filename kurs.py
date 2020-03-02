user_cur = input("kurs ")
user_qanak = int(input("shqam "))
user_cur2 = input("kurs2 ")
kurs_dict = {"USD": 1.3, "RUB": 86, "AMD": 611, "GBP": 1}

if user_cur in kurs_dict.keys():
    if user_cur2 in kurs_dict.keys():
        result = (kurs_dict[user_cur2] / kurs_dict[user_cur]) * user_qanak
print(result)
