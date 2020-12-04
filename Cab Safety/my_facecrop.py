import cv2
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
