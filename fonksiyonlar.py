#deneme
from matplotlib import pyplot as plt
import numpy as np
import math

def xrotate(x,y,aci):
    aci=math.pi*(aci/180)
    x=np.array(x)
    y=np.array(y)
    return (x*math.cos(aci))-(y*math.sin(aci))

def yrotate(x,y,aci):
    aci=math.pi*(aci/180)
    x=np.array(x)
    y=np.array(y)
    return (x*math.sin(aci))+(y*math.cos(aci))

def cokgen_yukseklik(a,aci,n):
    return (n*(((a-1))*math.tan(math.pi*(aci/180))/2)) #n katsayısı ihalar arasındaki mesafe içindir.

def create_shape(): #x ve y değerlerini tutan 2 matris
    x=[];
    y=[];
    kenarsayisi= int(input("kenar sayısı="))
    dis_aci= 360/kenarsayisi
    iha_sayisi=int(input("iha sayısı="))
    kenar_uzunluk=int(iha_sayisi/kenarsayisi)+1
    ic_aci= (180-dis_aci)/2
    a=kenar_uzunluk
    b=cokgen_yukseklik(kenar_uzunluk,ic_aci,2)
    aci_katsayi=1
    for i in range (kenar_uzunluk-1):
        a = a - 2
        x.append(a);
        y.append(b);
    fu=[x];
    fuu=[y];
    for i in range (kenarsayisi-1):
        kull_aci = aci_katsayi*dis_aci
        fx=xrotate(x,y,kull_aci)
        fy=yrotate(x,y,kull_aci)
        fu=np.append(fu,fx)
        fuu=np.append(fuu,fy)
        aci_katsayi= aci_katsayi+1
        i=i+1
    return fu,fuu

def create_main_line(): #ana dogrunun x ve y si
    x=[];
    y=[];
    kenarsayisi= int(input("kenar sayısı="))
    dis_aci= 360/kenarsayisi
    iha_sayisi=int(input("iha sayısı="))
    kenar_uzunluk=int(iha_sayisi/kenarsayisi)+1
    ic_aci= (180-dis_aci)/2
    a=kenar_uzunluk
    b=cokgen_yukseklik(kenar_uzunluk,ic_aci,2)
    aci_katsayi=1
    for i in range (kenar_uzunluk-1):
        a = a - 2
        x.append(a);
        y.append(b);
    return x,y

def cokgen_tanimlama():
    cokgen_adi = input("Çokgen adını giriniz = ")
    if cokgen_adi == "ucgen" or "üçgen" or "uçgen" or "ücgen":
        kenarsayisi = 3
    if cokgen_adi == "kare":
        kenarsayisi = 4
    if cokgen_adi == "besgen" or "beşgen":
        kenarsayisi = 5
    if cokgen_adi == "altıgen" or "altigen":
        kenarsayisi= 6
    if cokgen_adi == "yedigen" or "yedıgen":
        kenarsayisi = 7
    if cokgen_adi == "sekizgen" or "sekızgen":
        kenarsayisi = 8
    if cokgen_adi == "dokuzgen":
        kenarsayisi = 9
    if cokgen_adi == "ongen":
        kenarsayisi= 10
    if cokgen_adi == "daire":
        iha_sayisi= int(input("İha adedini giriniz.\n"))
        kenarsayisi=iha_sayisi
     
    return kenarsayisi
