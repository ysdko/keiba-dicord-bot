import sys
import cv2
import numpy as np
from PIL import Image
import pyocr
import pyocr.builders

#ある範囲を白画素化する関数
def draw_white(img, height1, height2, width1, width2):
    for i in range(height1, height2):
        for j in range(width1,width2):
            img[i, j] = 255

#ある範囲を黒画素化する関数
def draw_black(img, height1, height2, width1, width2):
    for i in range(height1, height2):
        for j in range(width1,width2):
            img[i, j] = 0


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

#画像読み込み
img = cv2.imread("./image/test3.png", 0)
height = img.shape[0]
width = img.shape[1]

#不要な文字削除(%とか)
draw_white(img, 0, height, 70, 95)
draw_white(img, 0, height, 115, 125)
draw_white(img, 0, height, 158, 175)
draw_white(img, 0, height, 180, width)

#画像切り取り(切り取った方が精度が上がるから)
img2 = img[20 : height-30, 80: 170]
imgl2 = img[20 : height-30, 80: 120]
imgr2 = img[20 : height-30, 115: 170]

#画像拡大
img3 = cv2.resize(img2 , (int(img2.shape[1]*2), int(img2.shape[0]*2)))
imgl3 = cv2.resize(imgl2 , (int(imgl2.shape[1]*2), int(imgl2.shape[0]*2)))
imgr3 = cv2.resize(imgr2 , (int(imgr2.shape[1]*2), int(imgr2.shape[0]*2)))

# 二値化(閾値100を超えた画素を255にする。)
threshold = 100
ret, img4 = cv2.threshold(img3, threshold, 255, cv2.THRESH_BINARY)
ret, imgl4 = cv2.threshold(imgl3, threshold, 255, cv2.THRESH_BINARY)
ret, imgr4 = cv2.threshold(imgr3, threshold, 255, cv2.THRESH_BINARY)

#膨張処理
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(img4, kernel, iterations=1)
erosionl = cv2.erode(imgl4, kernel, iterations=1)
erosionr = cv2.erode(imgr4, kernel, iterations=1)

#画像保存
cv2.imwrite('./image/new_test.png',erosion)
cv2.imwrite('./image/new_testl.png',erosionl)
cv2.imwrite('./image/new_testr.png',erosionr)

#馬番の文字認識
txtl = tool.image_to_string(
    #文字認識対象の画像image.pngを用意する
    Image.open("./image/new_testl.png"),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

#指数の文字認識
txtr = tool.image_to_string(
    #文字認識対象の画像image.pngを用意する
    Image.open("./image/new_testr.png"),
    lang="eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

#ご認識の空白や改行の削除
listsl = txtl.split()
listsr = txtr.split()

# nowl = ""
# nowr = ""
# listsl = []
# listsr = []
# for i in range(len(txtl)):
#     if txtl[i] != " " or txtl[i] != "¥n":
#         nowl += txtl[i]
#     else:
#         listsl[len(listsl)] = nowl
#         nowl = ""
# for i in range(len(txtr)):
#     if txtr[i] != " " or txtr[i] != "¥n":
#         nowr += txtr[i]
#     else:
#         listsr[len(listsr)] = nowr + " "
#         nowr = ""
# lists2l = listsl.split()
# lists2r = listsr.split()

#まとめて表示
for i in range(len(listsl)):
    print("馬番:"+ listsl[i] + "  " + "指数:" + listsr[i] + "%")

