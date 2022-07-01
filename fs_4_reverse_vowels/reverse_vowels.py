from re import S


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowel_index_list =[]
    vowel_list=[]
    lst = list(s)

    for index in range(len(s)):
        if s[index] in "aeiouAEIOU":
            vowel_list.append(s[index])
            vowel_index_list.append(index)

    for index in vowel_index_list:
        lst[index] = vowel_list.pop()
    
    return "".join(lst)



