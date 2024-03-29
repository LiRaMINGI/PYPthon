def number_to_words(num):
    ones = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
    elif num < 1000:
        return hundreds[num // 100] + ('' if num % 100 == 0 else ' ' + number_to_words(num % 100))
    else:
        return 'тысяча'


num = int(input("Введите число от 1 до 1000: "))
if 1 <= num <= 1000:
    print(number_to_words(num))
else:
    print("Число не входит в диапазон от 1 до 1000.")