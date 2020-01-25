import re
def find_duplicates(str):
    char_duplicate=0
    if str and str.strip():
        duplicates = {}
        for char in str:
            if char in duplicates:
                duplicates[char] += 1
                char_duplicate=1
            else:
                duplicates[char] = 1

        if (char_duplicate == 0):
            print("Tidak ada karakter berulang")
        else :
            for key, value in duplicates.items():
                if (value > 1) and (key != ' '):
                    print(key, ':', value, end="\n")
    else:
        print("Harus memasukan parameter dan harus string!")

# find_duplicates("hari apa saja saya bisa!")
# find_duplicates("cepat kerjakan!!!")
# find_duplicates(" ")
find_duplicates("adobe")