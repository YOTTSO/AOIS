def get_alphabet_indexes(char):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char = char.lower()  # Convert to lowercase for case-insensitive matching

    if char in alphabet:
        for i, c in enumerate(alphabet):
            if c == char:
                return i
    else:
        return 0

def function_of_hashing(str, number_of_elements):
    str = str.lower()
    resultat = 0
    length = len(str)
    for chri, el in enumerate(str):
        resultat += get_alphabet_indexes(el) * pow(26, length - 1 - chri)
    return resultat % number_of_elements

def add_elementus(key, elem):
     adding = [key, elem]
     hash = function_of_hashing(key, 5)
     table[hash].append(adding)

def del_elementus(key):
    hash = function_of_hashing(key, 5)
    elems = [pair[0] for pair in table[hash]]
    keyidx = elems.index(key)
    table[hash].pop(keyidx)

def print_our_table():
    for i, bucket in enumerate(table):
        print(f"Bucket {i}:")
        if len(bucket) == 0:
            print(f"Collisions :{len(bucket)}")
        else: print(f"Collisions :{len(bucket) - 1}")
        if not bucket:
            print("   <empty>")
        else:
            for key, elem in bucket:
                print(f"   Key: {key} - Element: {elem}")
        print("-" * 100)
    print('|' * 100)

TABLE_NUMBER_OF_ELEMENTS = 5
table = [[] for i in range(TABLE_NUMBER_OF_ELEMENTS)]
add_elementus('Bulgakov', 'Master and Margaret')
add_elementus('Orwell', '1984')
add_elementus('Dostoevsky', 'Crime and punishment')
add_elementus('Tolstoy', 'War and peace')
add_elementus('Dadzai', 'Confessions of an "inferior" person')
print_our_table()
del_elementus('Orwell')
print_our_table()