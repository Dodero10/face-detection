#detect face of images
import cv2
import os
image_path = '../img/peo10.jpg'















# face_detector = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')
#
# img = cv2.imread(image_path)
# img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# while True:
#     faces = face_detector.detectMultiScale(img_grey,1.3,5)
#     count = 0
#
#     for (x, y, w, h) in faces:
#         img_face_cut = cv2.resize(img[y + 2:y + h - 2, x + 2:x + w - 2],(64,64))
#         cv2.imwrite('img/peo1_{}.jpg'.format(count),img_face_cut)
#         cv2.rectangle(img, (x, y),(x+w,y+h),(0,255,0),2)
#         count +=1
#
#
#     cv2.imshow('FRAME', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWface_detector = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')
#
# img = cv2.imread(image_path)
# img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# while True:
#     faces = face_detector.detectMultiScale(img_grey,1.3,5)
#     count = 0
#
#     for (x, y, w, h) in faces:
#         img_face_cut = cv2.resize(img[y + 2:y + h - 2, x + 2:x + w - 2],(64,64))
#         cv2.imwrite('img/peo1_{}.jpg'.format(count),img_face_cut)
#         cv2.rectangle(img, (x, y),(x+w,y+h),(0,255,0),2)
#         count +=1
#
#
#     cv2.imshow('FRAME', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()