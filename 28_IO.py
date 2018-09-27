f = open("pliczek.txt","a+")#mogę też bez
f.write("123 ")
f.close()
#za każdym razem jak odświeżam, to dodaję kolejne + 123
# #io.UnsupportedOperation: not writable
# #dlaczego? w pierwszej komendzie - tryb otwarcia pliku "name" i mode, jeśli mode nie wpiszemy to on będzie "r" (domyślnie) czy możemy jedynie odczytywać plik
# #są inne tryby poza odczytywaniem.
# # jak damy run, to dopisze się do pliku obok "123

f = open("pliczek.txt","r") #zmieniam na R!
print(f.read(6)) #chujem
f.seek(12)
print(f.readline(6)) #kiewęże
f.close()

f = open("pliczek.txt","r")
for line in f.readlines():
    # print(line,end="") #usuń znak nowej linii END=""
    czysta_linia="asd  \n\n  ".rstrip() #rstrip usuwa wszystkie białe znaki(spacje?) z prawej =! lstrip, a strip z lewej i prawej
    print(line.rstrip()) #funkcja wypisuje cały pliczek.txt - for line in blebleble
f.close()
print(f.closed) #True
#READING FILES

def statistics(file):
    with open('pliczek.txt')as file:
        lines = file.readlines()
    return {'lines':len(lines),
            'words': sum(len(line.split(" "))for line in lines),
            'characters':sum(len(line)for line in lines)}


