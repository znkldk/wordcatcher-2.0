from translate import Translator
def diziyeAt(strng):
    dizi = []
    if (strng[0] != " "):
        strng=" "+strng
    if (strng[len(strng)-1] != " "):
        strng =strng + " "
    k = 0
    for i in range(1, len(strng)):
        if (strng[i] == " "):
            dizi.append(strng[k + 1:i])
            k = i
    return dizi
def kirp(strng):
    strng = strng.replace("\n","  ")
    strng = strng.replace("1", "")
    strng = strng.replace("2", "")
    strng = strng.replace("3", "")
    strng = strng.replace("4", "")
    strng = strng.replace("5", "")
    strng = strng.replace("6", "")
    strng = strng.replace("7", "")
    strng = strng.replace("8", "")
    strng = strng.replace("9", "")
    strng = strng.replace("0", "")
    strng = strng.replace(".", "")
    strng = strng.replace("?", "")
    strng = strng.replace("!", "")
    strng = strng.replace(",", "")
    strng = strng.replace(";", "")
    strng = strng.replace("-", "")
    strng = strng.replace("_", "")
    strng = strng.replace("*", "")
    strng = strng.replace(":", "")
    strng = strng.replace("<", "")
    strng = strng.replace(">", "")
    strng = strng.replace("+", "")
    strng = strng.replace("%", "")
    strng = strng.replace("/", "")
    strng = strng.replace("\"", "")
    strng = strng.replace("”", "")
    strng = strng.replace("“", "")
    strng = strng.replace(" ", ".")
    strng = strng.replace("..", ".")
    strng = strng.replace("..", ".")
    strng = strng.replace("..", ".")
    strng = strng.replace("..", ".")
    strng = strng.replace("..", ".")
    strng = strng.replace("..", ".")
    strng = strng.replace(".", " ")
    return strng
def mukerrerIgnere():
    cikartilacaklar=[]
    for i in range(0,len(ignore)):
        cnt=0

        for j in range(i,len(ignore)):
            if(ignore[i]==ignore[j]):
                if(cnt==1):
                    cikartilacaklar.append(j)
                cnt=cnt+1
    cikartilacaklar.sort()
    for i in range(0,len(cikartilacaklar)):
        ignore.pop(cikartilacaklar[i]-i)
def mukerrer():
    #Bir dizideki tekrar eden degerleri silmenin muhtemelen çok daha kolay yolları vardır ama ben o yolları bilmiyorum :)
    cikartilacaklar=[]
    for i in range(0,len(kelimeler)):
        cnt=0
        for j in range(i,len(kelimeler)):

            if(kelimeler[i]==kelimeler[j]):
                if(cnt==1):

                    cikartilacaklar.append(j)
                cnt=cnt+1
        count.append(cnt)
    cikartilacaklar.sort()
    for i in range(0,len(cikartilacaklar)):
        kelimeler.pop(cikartilacaklar[i]-i)
        count.pop(cikartilacaklar[i]-i)
def sirala():
    kelimeler.append(kelimeler[0])
    count.append(count[0])
    for i in range (0,len(kelimeler)):
        for j in range(i+1,len(kelimeler)):
            if(count[i]<count[j]):
                count[0]=count[j]
                count[j]=count[i]
                count[i]=count[0]
                kelimeler[0]=kelimeler[j]
                kelimeler[j]=kelimeler[i]
                kelimeler[i]=kelimeler[0]
    kelimeler.pop(0)
    count.pop(0)
def ilkHarfiBuyukYap():
    for i in range(0,len(kelimeler)):
        kelimeler[i]=kelimeler[i].capitalize()
        kelimeler[i] = kelimeler[i].replace("	", "")
    for i in range(0,len(ignore)):
        ignore[i]=ignore[i].capitalize()
        ignore[i] = ignore[i].replace("	", "")
def ignoreKelimeleriCikart():
    cikartilacaklar=[]

    for i in range(0,len(kelimeler)):


        for j in range(0,len(ignore)):

            if(str(kelimeler[i])==str(ignore[j])):
                cikartilacaklar.append(i)


    try:
        for i in range(0,len(cikartilacaklar)):
            kelimeler.pop(cikartilacaklar[i]-i)
            count.pop(cikartilacaklar[i]-i)
    except:
        print("Butun kelimeler çıkartıldı")
def ignoreKelimeleriAl():
    ignor = str(open("ignore.txt").read()) + " "
    ignor= ignor + str(open("sayilar.txt").read()) + " "
    ignor= ignor + str(open("isimler.txt").read()) + " "
    return ignor
# tanımlamalar
kelimeler = []
ignore=[]
count=[]
translator= Translator(to_lang="tr") #türkçe ye çevirmek için tanımlama yapılır

kelimeler =diziyeAt(kirp(open("text.txt").read()))#kelimeler çekilir
ignore =diziyeAt(kirp(ignoreKelimeleriAl()))

ilkHarfiBuyukYap() # kelimelerin yazımlarının düzenlenmesi için bütün kelimelerin ilk harfleri büyültülür kalan harfleri küçültülür.
mukerrer() #tekrar eden eden kelimeler ortadan kaldırılır
mukerrerIgnere() # mukerrer fonksiyonunun aynısı ama ıgnor dizisi için
sirala() # en çok tekrar eden kelimelerden en az tekrar eden kelimelere dizi sıralanır.
ignoreKelimeleriCikart() #ıgnore   olarak belirlediginiz kelimeler "kelimeler"  dizisinden çıkartılır

#for i in range (0,len(kelimeler)):
#    print(kelimeler[i])
for i in range (0,len(kelimeler)):
    print(kelimeler[i]+" = "+str(translator.translate(kelimeler[i]))+"   tekrar sayısı= "+str(count[i]))
