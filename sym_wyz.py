import random as r
import math as m
import sys
import time
import Algorytm_neh

def czytanie_z_pliku(plik_do_wczytania):
    tablica=[]
    text_file = open(plik_do_wczytania, "r+")
    for line in text_file.readlines():
         tablica.extend(line.split())
    ilosc_zadan=  int(tablica[0])
    ilosc_maszyn= int(tablica[1])
    index=2
    zadania_dla_maszyn = [[] for i in range(int(ilosc_maszyn))]

    while index < (ilosc_maszyn*ilosc_zadan +2):
        for k in range(ilosc_maszyn):
            zadania_dla_maszyn[k].append(tablica[index])
            index+=1
    text_file.close()
    return zadania_dla_maszyn, ilosc_zadan, ilosc_maszyn

def takMax(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return max(elem)
def takeFirst(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[0]
def takeSec(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[1]

lista, ilosc_z, ilosc_m = czytanie_z_pliku("ta000.txt")
lista1, ilosc_zad,ilosc_masz = czytanie_z_pliku("ta000.txt")
pi0 = Algorytm_neh.Neh(lista,ilosc_m,ilosc_z)

for i in range(len(lista)):
    r.shuffle(lista[i])
los=lista


def przepisanie_wart(tab):
    tab_temp = [[] for i in range(len(tab))]
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab_temp[i].insert(j,tab[i][j])
    return tab_temp

def swap(pi0,liczba_maszyn):
    czasy_na_maszynach = przepisanie_wart(pi0)
    miejsce_do_zamiany1, miejsce_do_zamiany2 = r.randint(0,len(pi0[0])-1), r.randint(0,len(pi0[0])-1)
    for i in range(liczba_maszyn):
        item2 = pi0[i][miejsce_do_zamiany1]
        pi0[i][miejsce_do_zamiany1] = pi0[i][miejsce_do_zamiany2]
        pi0[i][miejsce_do_zamiany2] = item2
    czasy_na_maszynach2 = przepisanie_wart(pi0)
    return czasy_na_maszynach, czasy_na_maszynach2

def insert(pi0,liczba_maszyn):
    czasy_na_maszynach = przepisanie_wart(pi0)
    miejsce_do_los, miejsce_do_wstaw = r.randint(0,len(pi0[0])-1), r.randint(0,len(pi0[0])-1)
    for i in range(liczba_maszyn):
        a=pi0[i].pop(miejsce_do_los)
        pi0[i].insert(miejsce_do_wstaw,a)
    czasy_na_maszynach2 = przepisanie_wart(pi0)
    return czasy_na_maszynach, czasy_na_maszynach2

def Cmax(lista, ilosc_maszyn):
    czas=[0] #czas poczatkowy dla kazdej maszyny
    for i in range(len(lista)-1):
        czas.append(int(lista[i][0])+czas[i])
    for ind in range(len(lista[0])):
        czas[0] += int(lista[0][ind])
        for k in range(ilosc_maszyn-1):
            if czas[k] > czas[k+1]:
                czas[k+1]=czas[k]
            czas[k + 1] += int(lista[k + 1][ind])
    return max(czas)

def prawdopodobienstwo(c,cprim,T):   
    if cprim >= c :
        p = m.exp((c-cprim)/T)
    else:
        p = 1
    return p

def prawdopodobienstwo2(c,cprim,T):
    p = m.exp((c-cprim)/T)
    return p



def wyzarzanie(pi0,T,Tmin,u,ilosc_maszyn):
    i = 1
    cpocz = Cmax(pi0,ilosc_maszyn)
    #print("kolejnosc",pi0)
    while(T > Tmin):
        czasy_na_maszynach, czasy_na_maszynach2 = swap(pi0,ilosc_maszyn)
        c = Cmax(czasy_na_maszynach,ilosc_maszyn)
        cprim = Cmax(czasy_na_maszynach2,ilosc_maszyn)
        p = prawdopodobienstwo(c,cprim,T)
        if p >= r.random():
            czasy_na_maszynach=czasy_na_maszynach2
            T = T*u
        else:
            T = T*u
        i += 1
    print("Liczba wykonan schladzania: ",i)
    print("Temperatura koncowa: ", T)
    print("Cmax poczatkowy: ", cpocz)
    print("Cmax wyzarzania: ",cprim)

T0 = 1000


def menu():
    #print("Antoni Sokolowski, Karolina Zienkiewicz - Symulowane wyzarzanie..")
    #time.sleep(1)
    choice = input("""
                          A: Kolejnosc poczotkowe generowana algorytmem Neh
                          B: Kolejnosc poczotkowa generowana losowa permutacja
                          C: Kolejnosc poczatkowa 1234.....
                          D: Quit/Log Out

                          PProsze wprowadzic wybor: """)

    if choice == "A" or choice == "a":
        wyzarzanie(pi0,T0,100,0.99,ilosc_m)
    elif choice == "B" or choice == "b":
        wyzarzanie(los, T0, 100, 0.999, ilosc_m)
    elif choice == "C" or choice == "c":
        wyzarzanie(lista1, T0, 100, 0.999, ilosc_m)
    elif choice == "D" or choice == "d":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")


def main():
    menu()

main()
