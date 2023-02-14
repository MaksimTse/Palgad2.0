from OmaMoodul import *

palgad=[1200.2333, 2500,750,395,1200]
inimesed=["A","B","C","E","D"]

while True:
    print(inimesed)
    print(palgad)
    print()
    menu=int(input("valik:\n1-lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Vähem palk\n5-Sort\n6-viige inimesi välja täiusliku salgataga\n7-otsi palka inimese nime järgi\n8-sisestatud palga põhjal kuvab inimeste madalamad ja kõrgemad palgad\n9-Leia top 3 vähem või rohkem\n10-Otsi keskmine palk ja kes on saada suurem\n11-Otsi maksuvaba palk\n12-Sort\n13-Otsige kes teenivad alla keskmise palga ja emalda nad\n14-Teeb nimekiri ilusam ja mugavam\n15-saate teada 5% tõusuga töötaja töötasu T-aastas\n16-Nimetage ümber iga 3 inimese järel \n"))
    if menu==0:
        break
    elif menu==1:
        inimesed, palgad=Lisa_andmed(inimesed, palgad)
    elif menu==2:
        imimesed,palgad=Kustutamine(inimesed, palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad)
        print("Suurim palk on",palk, nimi)
    elif menu==4:
        palk,nimi=Vähem_palk(inimesed,palgad)
        print("vähem palk pn", palk, nimi)
    elif menu==5:
        inimesed,palgad=Soorteerimine(inimesed,palgad)
    elif menu==6:
        iniemsed,palgad=Vordsed_palgad(inimesed,palgad)
    elif menu==7:
        iniemsed,palgad=imja(inimesed,palgad)
    elif menu==8:
        amount = int(input("Sisestage summa, millega võrrelda: "))
        more_than = disp(palgad, inimesed, amount, "suurim")
        less_than = disp(palgad, inimesed, amount, "vähem")
        print(f"Inimesed, kellel on palk rohkem kui {amount}:", more_than)
        print(f"Inimesed, kelle palk on väiksem kui {amount}:", less_than)
    elif menu==9:
        top(inimesed,palgad)
    elif menu==10:
        kesk(inimesed,palgad)
    elif menu==11:
        tulu(inimesed,palgad)
    elif menu==12:
        inimesed,palgad=sort(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=emalda(inimesed,palgad)
    elif menu==14:
        inimesed,palgad=kiri(inimesed,palgad)
    elif menu==15:
        inimesed,palgad=year(inimesed,palgad)
    elif menu==16:
        inimesed=rename(inimesed)
    else:
        print("Kirjuta õige arv")
