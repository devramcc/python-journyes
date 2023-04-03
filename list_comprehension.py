original_list = ['apple', 'banana', 'kiwi', 'grapefruit', 'pear', 'watermelon']
long_strings = [string for string in original_list if len(string) > 4]

for count, name in enumerate(original_list):
    print(f"{count}_{name}")


dict_comperhension = {name: len(name) for name in original_list if len(name) > 5}

print(dict_comperhension)