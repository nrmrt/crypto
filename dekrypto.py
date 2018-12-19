mainletters={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, \
         "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, \
         "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, \
         "z":26, " ":27, ".":28, ",":29, ";":30, "?":31, ":":32, "%":33, \
         "&":34, "(":35, ")":36, "{":37, "}":38, "/":39, "-":40, "_":41, \
         '"':42, "[":43, "]":44, "+":45, "^":46, "'":47, "<":48, ">":49, \
         "0":50, "1":52, "2":53, "3":54, "4":55, "5":56, "6":57, "7":58, \
         "8":59, "9":60, "*":61,"~":62}

readkry=open("krypto.txt","r")
solved=open("solved.txt","w")
keyr=open("key.txt","r")

exc=[]
groups={}
liner={}
count=0
for index,lines in enumerate(readkry.readlines()):
    for letter in lines:
        if letter=="O":
            if "\n" in exc:
                count+=1
                groups[count]="".join(exc)
                groups[count]=groups[count].split("\n")
                groups[count]="0b" + groups[count][1]
                groups[count]=int(groups[count],2)
                exc=[]
            else:
                count+=1
                groups[count]="".join(exc)
                groups[count]="0b" + groups[count]
                groups[count]=int(groups[count],2)
                exc=[]
        elif letter!="O":
            exc.append(letter)
    liner[index]=groups
    groups={}
    count=0
# not for first but other line beginings members has \n notation
#thats why it has two part if and else.we separete binaries with O
#on krypto code,if and elif used for that reason.Above part also binaries
# turned into 10 base numbers
key=keyr.readlines()
final=[]
keyind=0
for indexline,line in enumerate(liner.values()):
    for letters in line.values():
        if (letters-int(key[keyind]))<0:
            final.append((letters-int(key[keyind]))+62)
            keyind+=1            
        else:
            final.append(letters-int(key[keyind]))
            keyind+=1  
    liner[indexline]=final
    final=[]
    keyind+=1
#numbers which has turned into 10 base corrected using with key numbers.
keeper=[]
for line in liner.values():
    for number in line:
        for i in mainletters.keys():
            if number==mainletters[i]:
                keeper.append(i)
    keeper="".join(keeper)
    solved.write(str(keeper) + "\n")
    keeper=[]
# based on mainletters dict. the corrected numbers turned into letters
readkry.close()
solved.close()
keyr.close()