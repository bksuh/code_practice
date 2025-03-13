while True:
    try:
        line = input()
        translation_table = str.maketrans({
            'i': 'e',
            'e': 'i',
            'I': 'E',
            'E': 'I'
        })
        print(line.translate(translation_table))
    except:
        break