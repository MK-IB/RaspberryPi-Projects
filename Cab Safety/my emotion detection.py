from keras.models import load_model
from keras.preprocessing import image
import cv2
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

model = load_model('model25.h5')
def emotion_analysis(emotions,index):
    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    y_pos = np.arange(len(objects))
    
    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')
    
    plt.show()

    print(objects[index])
#croppingimage----------------------------
facedata = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(facedata)
img = cv2.imread('1.jpg')

try:
      
   minisize = (img.shape[1],img.shape[0])
   miniframe = cv2.resize(img, minisize)

   faces = cascade.detectMultiScale(miniframe)

   for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        sub_face = img[y:y+h, x:x+w]
          
        cv2.imwrite('cropped.jpg', sub_face)
              #print ("Writing: " + image)

except Exception as e:
     print (e)
#----------------------------------------
file = "cropped.jpg"
true_image = image.load_img(file)
img = image.load_img(file, grayscale=True, target_size=(48, 48))

x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)

x /= 255

custom = model.predict(x)

#---------------------------------------------
exp=list(custom)
expsep=list()
#exp=np.char.split(custom[0])
print(exp[0])
exp[0]=exp[0].tolist()
ind=exp[0].index(max(exp[0]))

emotion_analysis(custom[0],ind)
#----------------------------------------------
x = np.array(x, 'float32')
x = x.reshape([48, 48]);

plt.gray()
plt.imshow(true_image)
plt.show()

import os
try:
    os.remove("cropped.jpg")
except:pass    
