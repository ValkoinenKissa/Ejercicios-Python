"""
Imprime un bucle while los múltiplos de 2 comprendidos entre 1 y 10
"""

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i = i + 1

# Ahora con un bucle For

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
    i = i + 1
