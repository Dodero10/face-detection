#detect face of images

import cv2
import os

face_detector = cv2.CascadeClassifier('..\haarcascades\haarcascade_frontalface_alt.xml')
def getFaces(img_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img_gray,1.3,5)
    count = 0
    for (x, y, w, h) in faces:
        img_face_cut = cv2.resize(img[y:y + h,x:x + w],(64,64))
        cv2.imwrite('img/peo1_{}.jpg'.format(count),img_face_cut)
        count +=1

image_path = '..\img'

for file in os.listdir(image_path):
    file_path = os.path.join(image_path,file)
    for sub_file in os.listdir(file_path):
        img_path = os.path.join(file_path, sub_file)
        if not os.path.isdir(file_path.replace('img','img_faces')):
            os.mkdir(file_path.replace('img','img_faces'))




        if sub_file.endswith('.jpg'):
            getFaces(img_path)



cv2.destroyAllWindows()