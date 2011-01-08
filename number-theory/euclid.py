# encoding: utf-8

"""
Algoritmo de Euclides
Autor: Euclides de Alexandria
Tipo: Teoria dos números
Descrição: Algoritmo de Euclides em sua forma moderna. Computa o máximo
    divisor comum (MDC) entre dois números inteiros. Parte do princípio de
    que o MDC não muda se o menor número for subtraído do maior. [1] [2]
Complexidade:
    Pior caso: O(n^2), onde n é o número de dígitos da entrada. [3]
    O número de passos é no máximo
        log(max(a, b) * sqrt(5)) / log(phi),
    onde phi = 1.618... é a proporção áurea. [3]
Referências:
    [1] http://en.wikipedia.org/wiki/Euclidean_algorithm
    [2] http://pt.wikipedia.org/wiki/Algoritmo_de_Euclides
    [3] http://mathworld.wolfram.com/EuclideanAlgorithm.html
"""

def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(euclides(1071, 462))
