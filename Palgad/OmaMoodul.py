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
    b=input("Kelle nimi?: ")
    if b == "A":
        print ("A saab 1200")

    elif b == "B":
        print ("B saab 2500")

    elif b == "C":
        print ("C saab 750")
 
    elif b == "D":
        print ("A saab 395")

    elif b == "E":
        print ("E saab 1200")

    return i,p

def disp(palgad, inimesed, amount, compare):
    result = []
    for i in range(len(palgad)):
        if compare == "suurim" and palgad[i] > amount:
            result.append((inimesed[i], palgad[i]))
        elif compare == "vähem" and palgad[i] < amount:
            result.append((inimesed[i], palgad[i]))
    return result


