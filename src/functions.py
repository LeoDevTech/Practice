"""
1. Una cadena es un anagrama de otra si  Una cadena es un anagrama de otra si son anagramas. Las cadenas 'caro' y 'roca'
"""


def is_anagram(word_a: str, word_b: str):
    if len(word_a) == len(word_b):
        word_b = list(word_b)
        for letter in word_a:
            if letter in word_b:
                word_b.remove(letter)
                continue
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    print(is_anagram('roca', 'orca'))
    print(is_anagram('rocoso', 'orca'))
    print(is_anagram('rocoso', 'cosoro'))

"""
2.  Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python 
    tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""


def invert(frase: str):
    index = len(frase) - 1
    drow = ''
    while index > -1:
        drow += frase[index]
        index -= 1
    else:
        return drow


if __name__ == '__main__':
    print(invert('Hola mundo'))
    print(invert('estoy probando'))

"""
3. Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el 
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""


def is_palidromo(word: str):
    word = word.replace(' ', '')
    start = 0
    end = len(word) - 1
    while start <= end:
        if word[start] == word[end]:
            start += 1
            end -= 1
            continue
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    print(is_palidromo('sacas'))
    print(is_palidromo('radar'))
