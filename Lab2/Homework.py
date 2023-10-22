import math

#1.Find The greatest common divisor of multiple numbers read from the console.
def cmmdc(numbers):
    max_num = max(numbers) // 2
    ok = 0
    for i in range(max_num, 0, -1):
        for num in numbers :
            modu = num % i
            if modu != 0:
                ok = 0
                break
            ok = 1
        if ok == 1:
            return i
    return 1

#2.Write a script that calculates how many vowels are in a string.
def nr_voc(cuvant):
    vocale = "aeiouAEIOU"
    nr_vocale = 0
    for lit in cuvant:
        if lit in vocale:
            nr_vocale += 1
    return nr_vocale

#3.Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def subsir_in_sir(sir_mic, sir_mare):
    count = 0
    len_mic = len(sir_mic)
    len_mare = len(sir_mare)
    for lit in range(len_mare):
        if sir_mare[lit: (lit + len(sir_mic))] == sir_mic:
            count += 1
    return count

#4.Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def conversie_anglia(cuvant):
    #ccbj = cuvant_cu_bare_jos
    ccbj = ""
    len_cuv = len(cuvant)
    for lit in range(len_cuv):
        if cuvant[lit].isUpper():
            if lit == 0:
                ccbj += cuvant[lit].lower()
            else:
                ccbj += "_" + cuvant[lit].lower()
        else:
            ccbj += cuvant[lit]
    return ccbj

#5.Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order.
#def ordine_ciudata_spiralata(matrice):
    #nu stiu, revin mai tarziu

#6.Write a function that validates if a number is a palindrome.
def palindromastic(numar):
    numari = str(numar)
    length = len(numari)
    for lit in range(length // 2, 0, +1):
        if numari[lit] != numari[length-1 - lit]:
            return False
    return True

#7.Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
def extrage_numarul(sir_de_c):
    lenn = len(sir_de_c)
    numar = ""
    for i in range(lenn, 0, +1):
        if sir_de_c[i].isDigit():
            numar += sir_de_c[i]
    return numar

#8.Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def cati_1_sunt(numar):
    count = 0
    numarul_binar = bin(numar)
    #also: count = numarul_binar.count('1')
    sirul_binar = str(numarul_binar)
    for lit in sirul_binar:
        if lit == '1':
            count += 1
    return count

#9.Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def cea_mai_folosita_litera(sir_de_c):
    vector_de_frecv = [0] * 26
    sir_de_c = sir_de_c.lower()
    for lit in sir_de_c:
        vector_de_frecv[ord(lit) - ord('a')] += 1
    cele_mai_multe_instante = max(vector_de_frecv)
    for i in range(26, 0, +1): #also: for i in range(26), bcs it's by deafult (26, 0, +1)
        if vector_de_frecv[i] == cele_mai_multe_instante:
            return chr(i + ord('a'))
        
#10.Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.
def num_words(sir_de_c):
    cuvinte = sir_de_c.split()
    numere_cuvinte = len(cuvinte)
    return numere_cuvinte

#Done.