import cv2 as cv
from rescale import *
"""PATH"""
res = "resources"
vid_path = res +"/Videos/"
img_path = res + "/Images/"
face_path = res + "/Faces/"

"""Image Read"""
# img1  = cv.imread('resources/Photos/cat.jpg')
# img2  = cv.imread('resources/Photos/cat_large.jpg')

# cv.imshow('Cat',img1)
# cv.waitKey(0)

# cv.imshow('Large Cat not visible',img2)
# cv.waitKey(0)

"""Video Read"""
# capture = cv.VideoCapture(f"{vid_path}dog.mp4")
# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('Video',frame)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
#  # error: (-215:Assertion failed) means no image at path (in this case vid ran out of frames)


# capture.release()
# cv.destroyAllWindows()



capture = cv.VideoCapture(f"{vid_path}dog.mp4")
resized_capture  = changeRes(capture,144,255)
while True:
    isTrue,frame = resized_capture.read()

    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()


img1 = cv.read(f"{img_path}cat_large.jpg")
resized_img1 = rescaleFrame(img1)
cv.imshow(img1)
capture
cv.imshow(resized_img1)
