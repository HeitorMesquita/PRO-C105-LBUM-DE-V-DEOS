import cv2
import os

path = "Images"

Image = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path + "/" + file
        print(file_name)
        Image.append(file_name)

print(len(Image))
count = len(Image)

frame = cv2.imread(Image[0])
height,width,channels = frame.shape
size = (width,height)

print(size)

Out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*"DIVX"),0.8,(width,height))

# for i in range(count-1,0,-1):
for i in range(0, count -1):
    frame = cv2.imread(Image[i])
    Out.write(frame)

Out.release()

print("Concluído")