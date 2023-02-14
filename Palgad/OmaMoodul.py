def Lisa_andmed(i:list,p:list):
    """Inimese ja tema palga lisamine nimekirja
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: list, list
    """

    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def Kustutamine(i:list,p:list):
    """Inimese ja tema palga eemaldamine nimekirjast
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: list, list 
    """

    nimi=(input("Sisesta nimi "))
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
        return i,p


def Suurim_palk(i:list,p:list):
    """Maksimaalse palga leidmine
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """

    # ise kirjutada, kui mitu palka
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]

    return palk,nimi

def Vähem_palk(i:list,p:list):
    """Minimalsem palga leidmine
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """

    # ise kirjutada, kui mitu palka
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]

    return palk,nimi

def Soorteerimine(i:list,p:list):
    """Sorteeri palga järgi
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: int, str
    """
    v=int(input("palk 1-kahaneb, 2-kasvab? "))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi

    return i,p

def Vordsed_palgad(i:list,p:list):
    """Sorteeri palga järgi
    :param list i: Inimeste järend
    :param list p: Palgade järend
    :rtype: list, list
    """
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid)) #[1200, 2500,750,750,1200]->[1200,700]
    for palk in dublikatid:
        n=p.count(palk) #1200, n=2; 750, n=2
        k=-1
        print(palk)
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi,"saab kätte",palk)
    return i,p

def imja(i:list,p:list):
    """leiab nime ja oma palga
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Kelle palk tahad leia? \n")
    while nimi not in i:
        nimi=input("Palun kirjuta õige nimi \n")
    n=i.count(nimi)
    if n!=1:
        print(f'Siin on mõned inimesed kes nimi on {nimi} \n')
        kopia=i.copy()
        for j in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,'')
            print(f'{j+1} {nimi} saab {p[ind]} \n')
    else:
        ind=i.index(nimi)
        print(f'{nimi} saab {p[ind]} \n')
    return i,p

def disp(palgad, inimesed, amount, compare):
    result = []
    for i in range(len(palgad)):
        if compare == "suurim" and palgad[i] > amount:
            result.append((inimesed[i], palgad[i]))
        elif compare == "vähem" and palgad[i] < amount:
            result.append((inimesed[i], palgad[i]))
    return result

def top(i:list,p:list): 
    """top 3 vähem ja rohkem
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(min(kopia))
        print(f"{i+1} inimene - {i[ind]} saab väikse palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(max(kopia))
        print(f"{j+1} inimene - {i[ind]} saab suur palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(p)+1)

def kesk(i:list,p:list): 
    """leiab keskmine palk
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    kesk=sum(p)/len(p)
    print(f"Keskmine palk on {kesk}")
    for j in range(len(i)):
        if p[j]>=kesk:
            print(f"{i[j]} saab suurem kui keskmine palk, ta saab {p[j]}")

def tulu(i:list,p:list): 
    """leiab maksuvaba
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    for j in range(0,len(p)):
        if i[j]<500:
            palk=p[j]
        elif 500>=p[i]<=1200:
            palk=(p[i]-500)-(p[j]-500)*0.2
        elif 1200>p[i]>=2099:
            palk=(500-(5/9)*(p[j]-1200))-(500-(5/9)*(p[j]-1200))*0.2
        else:
            palk=p[j]*0.2
        print(f"{i[j]} on maksuvaba palk {palk}")

def sort(i:list,p:list):
    """Sorteeri palga ja inimeste järgi
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    vali=input("Sorteeri nime (1) või palga järgi (2) ")
    while vali not in ["1","2"]:
        vali=input("Kirjuta ainult 1 või 2 ")
    if vali=="1":
        vali_2=input("A–Ü või Ü–A ").upper()
        while vali_2 not in ["A-Ü","Ü-A"]:
            vali_2=input("A–Ü või Ü–A ").upper()
        for l in range(0,len(i)):
            for o in range(0,len(i)):
                if i[l]==i[o] and l!=o:
                    for u in range(0,len(i)):
                        i[o]+=f"_{u+1}"
                        break
        kopia=i.copy()
        i.sort()
        p1=[]
        for j in range(0,len(i)):
            ind=kopia.index(i[j])
            p1.insert(j,p[ind])
        p=p1
        if vali_2=="Ü-A":
            i.reverse()
            p.reverse()
    else:
        for l in range(0,len(i)):
            for o in range(0,len(i)):
                if p[l]<p[o]:
                    abi=p[l]
                    p[l]=p[o]
                    p[o]=abi
                    abi=i[l]
                    i[l]=i[o]
                    i[o]=abi
        vali_2=input("Kasvav või kahanev järjekord? ").title()
        while vali_2 not in ["Kasvav","Kahanev"]:
            vali_2=input("Ainult Kasvav või kahanev! ").title()
        if vali_2=="Kahanev":
            i.reverse()
            p.reverse()
    return i,p 

def emalda(i:list,p:list):
    """enmaldab kes palk on vähem kui keskmine
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    i1=[] 
    p1=[]
    kesk=sum(p)/len(p)
    print(f"Keskmine palk on {kesk}")
    for j in range(0,len(i)):
        if p[j]>kesk:
            p1.append(p[j])
            i1.append(i[j])
    i=i1 
    p=p1
    return i,p

def kiri(i:list,p:list):
    """teeb nimekiri ilusam
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    for j in range(0,len(i)):
        i[j]=i[j].title()
        p[j]=round(p[j],1) 
        p[j]=int(p[j])
        return i,p

def year(i:list,p:list):
    """töötasu arvestus T-aastas
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    T = int(input('Mitu aastat? '))
    N = int(input('Mis on selle inimese number, kelle palka soovite teada? '))
    for d in range(N-1,len(i)):
        de=i[d]
        for j in range(N-1,len(p),1):
            p[j] = p[j] * 1.05 ** T
        print('-----------------------')
        print(f'{de} palk {T} aasta pärast on {round(p[j],2)}')
        return i,p

def rename(i:list):
    """ümbernimetamine
    :param list i: Inimeste järjend
    :rtype: list
    """
    for j in range(2,len(i),3):
        ren=input("Kirjuta uus nimi: ")
        while ren.isdigit() or len(ren)<1:
            ren=input("Kirjuta õige nimi: ")
        i.pop(j)
        i.insert(j,ren)
    return i
