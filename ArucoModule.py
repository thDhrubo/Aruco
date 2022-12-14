import cv2
import cv2.aruco as aruco
import numpy
import os
class sum:
    t1=0
    t2=0
def findArucoMarkers(image,markerSize=5,totalMarkers=250,draw=True):
    imgGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict=aruco.Dictionary_get(key)
    arucoParam= aruco.DetectorParameters_create()
    corners,ids,rejected=aruco.detectMarkers(imgGray,arucoDict,parameters=arucoParam)
    print(ids[0])
    if draw:
        aruco.drawDetectedMarkers(image,corners)
    if len(corners) > 0:
        # flatten the ArUco IDs list
        ids = ids.flatten()
        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)

            check=False
            if markerID==1:
                sum.t1+=cX
                sum.t2+=cY
                check = True
            if markerID==2:
                sum.t1 += cX
                sum.t2 += cY

            print(cX,cY)
            print(sum.t1,sum.t2)
            cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
            # draw the ArUco marker ID on the image
            cv2.putText(image, str(markerID),
                        (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            print("[INFO] ArUco marker ID: {}".format(markerID))
            if check:
                cv2.circle(image,(sum.t1//2,sum.t2//2),4,(0,0,255),-1)


def main():

    img = cv2.imread('Aruco.jpg', 1)
    findArucoMarkers(img)
    # Loop Through all markerts and augment each one
    cv2.imshow("Image",img)
    cv2.waitKey(500000)


if __name__=="__main__":
    main()
