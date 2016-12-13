#coding=utf-8  
import cv2
import time
if __name__ == '__main__':   
	cv2.namedWindow("camera",1)  
	#开启ip摄像头  
	video="http://admin:admin@192.168.1.101:8081/"  
	cap = cv2.VideoCapture(video)
	num = 0;  
	while(cap.isOpened()):
		ret, frame = cap.read()

		cv2.imshow("camera",frame)

		#按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口  
		key = cv2.waitKey(10)     
		if key == 27:  
			#esc键退出  
			print "esc break..."
			break  
		if key == ord(' '):  
		#保存一张图像  
			num = num+1  
			filename = "frames_%s.jpg" % num  
			cv2.imwrite(filename,frame)  
	cap.release()
	cv2.destroyAllWindows()