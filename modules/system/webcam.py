import cv2

def Selfie(): 
	try:
	    cap = cv2.VideoCapture(0)
	    for i in range(30):
	        cap.read()
	    ret, frame = cap.read()
	    cv2.imwrite(r'C:\hesoyam8927163\webcam.png', frame)   
	    cap.release()
	except:
	    pass