#imports
from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
import numpy as np
import glob
import os


mypath='./segmentasyon_haritası/'#boyutlaandıracğımız dosyanın uzantısı
os.mkdir("ResizedSegmentasyon_haritasi")#boyutlandırdığımız fotografların kaydedileceği yol
folderLen=len(mypath)

for img in glob.glob(mypath+"/*.jpg"):
  image=cv2.imread(img)
  imgResized=cv2.resize(image,(1024,1024))
  cv2.imwrite("ResizedSegmentasyon_haritasi/"+img[folderLen:],imgResized)
  cv2.imshow("image", imgResized)
  cv2.waitKey(1)
cv2.destroyAllWindows()




