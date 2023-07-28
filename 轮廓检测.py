import cv2
img = cv2.imread('shape.jpg')
imgContour = img.copy()
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#图片的黑白化
canny = cv2.Canny(img,150,200)#检测边缘
contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#侦测轮廓
#上面一个是轮廓 一个是阶层
for cnt in contours:#for loop 跑过所有侦测了的轮廓
    cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)#画轮廓 -1是每个都画 4是粗度
    area = cv2.contourArea(cnt)#轮廓面积
    if area > 500:
        peri = cv2.arcLength(cnt,True)#外框总长 boolean指的是是否闭合
        # print(cv2.contourArea(cnt))
        # print(cv2.arcLength(cnt,True))
        vertices = cv2.approxPolyDP(cnt,peri*0.02,True)#近似轮廓 第二个是近似值 boolean指的是是否闭合
        corners = (len(vertices))#顶点
        x,y,w,h = cv2.boundingRect(vertices)#顶点的坐标
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),4)#用方形把每个图形框起来 (x,y)是方形左上角坐标 (x+w,y+h)是方形右下角坐标
        if corners == 3:
            cv2.putText(imgContour,'Triangle',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2) #写文字
        elif corners == 4:
            cv2.putText(imgContour,'Rectangle',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 5:
            cv2.putText(imgContour,'Pentagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 6:
            cv2.putText(imgContour,'Hexagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 7:
            cv2.putText(imgContour,'Heptagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 8:
            cv2.putText(imgContour,'Octagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 9:
            cv2.putText(imgContour,'Nonagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        elif corners == 10:
            cv2.putText(imgContour,'Decagon',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgContour',imgContour)
cv2.waitKey(0)