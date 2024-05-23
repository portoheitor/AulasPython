'''
Interavel -> str, range, etc
interador -> quem sabe entregar um valor por vez
next -> me entregue o proximo
inter -> me entregue seu valor

'''

texto = 'Heitor'
interador = iter(texto)

while True:
    try:
        letra = next(interador)
        print(letra)
    except StopIteration:
        break

    #Mesma coisa que fazer isso abaixo 
# for letra in texto:
    # print(letra)

