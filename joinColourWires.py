import os
import cv2
#take a screenshot
os.system("adb shell screencap -p //sdcard//tt1.png & adb pull //sdcard//tt1.png D://amongustest//pythonTestPull.png");
#pull screenshot from phone
#os.system("adb pull //sdcard//tt1.png D://amongustest//pythonTestPull.png");

#read image in openCV
img = cv2.imread("D:\\amongustest\\pythonTestPull.png");

#define all wire cordiante points
leftPoints = ((546,181),(546,306),(546,431),(546,556),(1040,182),(1040,307),(1040,430),(1040,553));
rightPoints = ((1040,182),(1040,307),(1040,430),(1040,553));

print(img[leftPoints[0][1],leftPoints[0][0]]);
command = '';
for i in range(4):
    temp =  img[leftPoints[i][1],leftPoints[i][0]];
    for j in range(4):
        if (temp == img[rightPoints[j][1],rightPoints[j][0]]).all():
            command += "adb shell input swipe "+str(leftPoints[i][0])+" "+str(leftPoints[i][1])+" "+str(rightPoints[j][0])+" "+str(rightPoints[j][1]);
    print("\n"+command);
    command += " & ";
os.system(command);
