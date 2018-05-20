import cv2,shutil

src = "./l.png"
to = "./lighter/"
a = "./lighter/0.pgm"
img = cv2.imread(src,cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(100,40))
cv2.imwrite(a,img)
for i in range(1,500):
    shutil.copyfile(a,to+"%d.pgm" %(i))