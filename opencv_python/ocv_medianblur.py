#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys

print(sys.argv[0])
arg=68
e1 = cv2.getTickCount()
if (len(sys.argv)==2):
    if sys.argv[1]=="-h":
      print """Kullaım : ./ocv1.py DOSYA sayı (sayı>5 ve sayı çift olmalı) """
      sys.exit(0)
    if sys.argv[1]=="-v":
      print "Sürüm : 1.0"
      sys.exit(0)
    else:
      img=cv2.imread(sys.argv[1])
elif (len(sys.argv)==3):
    img=cv2.imread(sys.argv[1])
    arg=sys.argv[2]
else:
    print "yardım için -h parametresini kullanın\n"
for i in xrange(5,int(arg),2):
    img = cv2.medianBlur(img,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(10)&0xFF
    if k==27:#1048603 :     Esc key to stop
        break
    elif k== ord('s'):#1048691 :  # "s" düğmesine basıldığında kayıt yap
        print("kayıt yapılıyor...\n")
        if cv2.imwrite('141.png',img):
            print("kayıt yapıldı.\n")
            break
	else:
	    print("kayıt yapılamadı.\nTekrar deneyin...\n")
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print k # else print its value
    print k

cv2.destroyAllWindows()
