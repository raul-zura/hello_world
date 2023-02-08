# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:36:00 2023

@author: raulz
"""

#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. When decrypting the message, it's
#relatively easy to tell from context whether a letter is
#meant to be an i or a j.
#
#To encrypt a message, we first remove all non-letters and
#convert the entire message to the same case. Then, we break
#the message into pairs. For example, imagine we wanted to
#encrypt the message "PS. Hello, worlds". First, we could
#convert it to PSHELLOWORLDS, and then break it into letter
#pairs: PS HE LL OW OR LD S. If there is an odd number of
#characters, we add X to the end.
#
#Then, for each pair of letters, we locate both letters in
#the cipher square. There are four possible orientations
#for the pair of letters: they could be in different rows
#and columns (the "rectangle" case), they could be in the
#same row but different columns (the "row" case), they could
#be in the same column but different rows (the "column"
#case), or they could be the same letter (the "same" case).
#
#Looking at the message PS HE LL OW OR LD SX:
#
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal. When decrypting, it
#would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.
#
#What we do for each of the other three cases is different:
#
# - For the Rectangle case, we replace each letter with
#   the letter in the same row, but the other letter's
#   column. For example, we would replace HE with GR:
#   G is in the same row as H but the same column as E,
#   and R is in the same row as E but the same column as
#   H. For another example, CS would become KL: K is in
#   C's row but S's column, and L is in C's column but S's
#   row.
# - For the Row case, we pick the letter to the right of
#   each letter, wrapping around the end of the row if we
#   need to. PS becomes QL: Q is to the right of P, and L
#   is to the right of S if we wrap around the end of the
#   row.
# - For the Column case, we pick the letter below each
#   letter, wrapping around if necessary. LD becomes TY:
#   T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#
#Decrypting a message is essentially the same process.
#You would use the exact same cipher and process, except
#for the Row and Column cases, you would shift left and up
#instead of right and down.
#
#Write two methods: encrypt and decrypt. encrypt should
#take as input a string, and return an encrypted version
#of it according to the rules above.
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - Add an X to the end if the length if odd.
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
# - Encrypt it.
#
#decrypt should, in turn, take as input a string and
#return the unencrypted version, just undoing the last
#step. You don't need to worry about Js and Is, duplicate
#letters, or odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"
#
#HINT: You might find it easier if you implement some
#helper functions, like a find_letter function that
#returns the row and column of a letter in the cipher.
#
#HINT 2: Once you've written encrypt, decrypt should
#be trivial: try to think of how you can modify encrypt
#to serve as decrypt.
#
#To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



#Add your code here!
def  encrypt(st):
    #cambio a mayusculas todas las letras
    st2 = st.upper()
    
    #reemplazo las j por i
    st2= st2.replace("j", "i") 
    st3 = st2
    
    chars = ".-/\?,_!{}[]^ "
    
    #reemplazo los caracteres especiales por una cadena vacia
    for i in st2:
        
        if i in chars:
            st3 = st3.replace(i, "")
            
    l = len(st3)
    
    #agrego a la cadena de caracteres una X en caso que el numero de letras sea impar
    if l % 2 != 0:
        st3 += "X"
    
    #llamo la funcion pairs
    p = pairs(st3)
    
    p2 = []
    
    #en caso la primera letra de una pareja sea igual a la segunda letra
    #la segunda se sustituye por X
    for i in p:
        
        if i[0] == i[1]:
            i = i[0]+"X"
    
        p2.append(i)
    
    #print(p2)
    
    #pair_p=p[0]
    
    p3 = []
    
    #llamo a la funcion case_select, con los argumentos pair y "E"
    for pair in p2:
        st4 = case_select(pair,"E")
        
        p3.append(st4)
    
    #uno las letras en una sola cadenas de caracteres
    st5 = "".join(p3)
    
    return st5


def  decrypt(st):
    #paso a mayusculas todas las letras
    st2 = st.upper()
    
    
    #obtengo las parejas de letras de la funcion pairs
    p = pairs(st2)
    
    p2 = []
        
    #llamo la funcion case_select, con los argumentos pair y "D"
    for pair in p:
        st3 = case_select(pair,"D")
        
        p2.append(st3)
    
    #uno las letras en una sola cadena de caracteres
    st4 = "".join(p2)
    
    return st4
    

def pairs(st):
    
    l = []

    for i in range(len(st)):
        
        #verifico que el contador no ha llegado a la ultima pareja
        if i != len(st)-1:
            # en el caso que el contador sea distinto de 0 y que sea par
            #hago una seleccion de la cadena original st y agrego dicha
            #seleccion de letras a la lista l
            #Aqui tomo los caracteres que estan entre 1 y 2 caracteres de distancia
            #con respecto al contador
            if i!=0 and i%2 ==0:
                pair = st[i-2:i]
                l.append(pair)
        else:
            #si el contador llega al final de la cadena, vuelvo a hacer
            #una seleccion con la diferencia que toma el caracter inmediatamente
            #anterior y el ultimo caracter
            pair = st[i-1:]
            l.append(pair)

    return l


def find_letter(letter):
    
    for i in range(len(CIPHER)):
        #elijo la fila de la tupla de tuplas CIPHER
        row = CIPHER[i]
        
        #Uno los caracteres de esa tupla
        st = "".join(row)
        
        #print(st)
        
        #guardo el valor de columna. Si dicho valor se encuentra el metodo
        #devolvera un valor entre 0 y 4. Si no se encuentra devolvera un valor
        #de -1
        col_i = st.find(letter)
        
        row_i = i
        #print(i)
            
        
        #print(y)
            
        #Si el valor es diferente a -1, la funcion devolvera el valor
        #de los indices de la columna y de la fila
        if col_i != -1:
            return col_i, row_i


def case_select(pair,c):
    
    #l1 se refiere al caracter de la izquierda de la pareja de letras
    #l2 se refiere al caracter de la derecha de la pareja de letras
    l1 = pair[0]
    l2 = pair[1]
    
    #obtengo los indices de la columna y fila de la primera y segunda letra
    col1, row1= find_letter(l1)
    
    col2, row2 = find_letter(l2)
    
    st = ""
    #print(x1, y1)
    #print(x2, y2)
    
    #verifico si las letras se encuentran en la misma fila, columna o si se trata
    #de un caso rectangle
    if col1 == col2 and row1 != row2:
        st = "column"
    elif col1 != col2 and row1 == row2:
        st = "row"
    elif col1 != col2 and row1 != row2:
        st = "rectangle"
    
    # x1A = 6
    # y1A = 6
    # x2A = 6
    # y2A = 6
    #print(st)
    
    #Si se ocupa la funcion encript el valor sera "E". Si se ocupa decript
    #el valor de c sera "D"
    if c == "E":
        va = 1
        numl1 = 4
        numl2 = 0
    else:
        va = -1
        numl1 = 0
        numl2 = 4
    
    #Asigno a row1A, row2A, col1A y col2A los nuevos valores de las letras
    #a encriptar (si c es "E") o a desencriptar (si c es "D")
    if st == "row":
        #Si es el row case, entonces los valores de fila seran los mismos
        row1A = row1
        row2A = row1
        
        #los valores de columna variaran. En caso que c sea "E" al valor del
        #indice de la columna se le sumara 1. Si c es "D" se le restara 1.
        
        if col1 != numl1:
            col1A = col1 + va
            
        else:
            col1A = numl2
        
        if col2 != numl1:
            col2A = col2 + va
                        
        else:
            col2A = numl2
            #print("This is x2A")
            #print(x2A)
            
    elif st == "column":
        #Si es el column case, los valores de columna no variaran para las letras
        col1A = col1 
        col2A = col1
        
        #los valores de fila variaran. En caso que c sea "E" el valor del indice de 
        #fila se le sumara 1. Si c es "D" se le restara 1
        
        if row1 != numl1:
            row1A  = row1 +va
        
        else:
            row1A = numl2
            
        if row2 != numl1:
            row2A = row2 +va
        
        else:
            row2A = numl2
    
    elif st == "rectangle":
        #el procedimiento a seguir tanto para c = "E" y para c = "D" es el mismo        
        
        row1A = row1
        col1A = col2
        
        row2A = row2 
        col2A = col1
    
    #print(x1A)
    
    l1A = CIPHER[row1A][col1A]
    l2A = CIPHER[row2A][col2A]
    
    return l1A + l2A

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))
