import random
letters={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, \
         "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, \
         "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, \
         "z":26, " ":27, ".":28, ",":29, ";":30, "?":31, ":":32, "%":33, \
         "&":34, "(":35, ")":36, "{":37, "}":38, "/":39, "-":40, "_":41, \
         '"':42, "[":43, "]":44, "+":45, "^":46, "'":47, "<":48, ">":49, \
         "0":50, "1":52, "2":53, "3":54, "4":55, "5":56, "6":57, "7":58, \
         "8":59, "9":60, "*":61,"~":62}

guardian={}
reader=open("deneme.txt","r")
key=open("key.txt","w")
kmsg=open("krypto.txt","w")

for index,line in enumerate(reader.readlines()):
    holder=[]
    for item in line.lower():
        decis=random.randint(1,62)
        key.write(str(decis)+"\n")
        for k in letters.keys():
            if item==k:
                holder.append(bin((letters[k]+decis)%62))
    guardian[index]=holder
#Above part, random number for each letter created and saved, and shifting done respect to
#this random number for each letter.Each letter has specific random shifting!
#text document was read line by line and each letter shifted, key values saved and
#binary number translation done on the shifted letters.
for keys_of_guard in guardian.keys():
    extracter=[]
    if keys_of_guard!=0:
        kmsg.write("\n")
#if not equal zero ensures new line
    for index,item in enumerate(guardian[keys_of_guard]):
        extracter.append(item.split("0b"))
        kmsg.write(str(extracter[index][1])+"O")
# 0b notation on the binary numbers were erased and when we done splitting
# it creates 2 member list we took second one which is indicates binaries not
# 0b's.
reader.close()
key.close()
kmsg.close()