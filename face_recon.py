import numpy as np
import cv2
import os
from PIL import Image

try:
    os.mkdir("user_txt")
    print("user_txt is create")
except:
    print("user_txt is exsit!")

try:
    os.mkdir("dataset")
    print("dataset is create")
except:
    print("dataset is exsit!")

try:
    os.mkdir("recognizer")
    print("recognizer is create")
except:
    print("recognizer is exsit!")
#######################################

def data_set(user_id,name):

    f = open("user_txt/"+user_id+".spw","w")
    f.write(name)
    f.close()

    face = cv2.CascadeClassifier('face.xml')

    cam = cv2.VideoCapture(0)
    #u_id = input("enter user id : ")
    #os.mkdir("dataset/user/"+user_id)
    s_code = 0
    while (1):
        _,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,1.3,5)

        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

            img2 = gray[y:y+h,x:x+w]

            cv2.imwrite("dataset/_"+user_id+"_"+str(s_code)+".jpg",img2)
            #cv2.imshow("face",img2)
            s_code = s_code+1
            

        cv2.imshow("my_face",img)

        if (cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()    


def train():
    recon = cv2.face.LBPHFaceRecognizer_create();
    path = "dataset"

    faces = []
    IDs = []

    allimagepath = [os.path.join(path,f) for f in os.listdir(path)]
    #print (allimagepath)
    for imagepath in allimagepath:
        face_img = Image.open(imagepath).convert('L')
        face_np = np.array(face_img,'uint8')
        ID = int(os.path.split(imagepath)[-1].split("_")[1])

        faces.append(face_np)
        IDs.append(ID)
        # print(IDs)
        cv2.imshow("face_train",face_np)
        cv2.waitKey(10)
        # cv2.destroyAllWindows()

    #print(faces)
    recon.train(faces,np.array(IDs))
    recon.save("recognizer/train_data.yml")

    cv2.destroyAllWindows()
        #return faces,IDs
        # print(faces)

 
def detector():

    face = cv2.CascadeClassifier('face.xml')
    cam = cv2.VideoCapture(0)

    rec = cv2.face.LBPHFaceRecognizer_create();
    try:
        rec.read('recognizer/train_data.yml')
    except:
        print("train data not exsit!")
    Id =0

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    while (1):
        _,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,1.3,5)

        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            #ana wakiya
            Id,conf = rec.predict(gray[y:y+h,x:x+w])

            # 
            # set id
            cv2.putText(img,"ID : "+str(Id),(x,y+h+25),font,0.8,(255,0,0),2,cv2.LINE_AA)
            # 

            f = open("user_txt/"+str(Id)+".spw","r")
            user_name = f.readline()
            f.close()

            cv2.putText(img,"name : "+user_name,(x,y+h+45),font,0.8,(255,0,0),2,cv2.LINE_AA)



            

        cv2.imshow("my_face",img)

        if (cv2.waitKey(1) == ord('q')):
            #cam.release()
            break
    cam.release()





    
    cv2.destroyAllWindows()   























