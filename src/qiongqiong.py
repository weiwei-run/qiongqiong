# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# 自定义数据集读取
import readJson
import detect

root = tk.Tk()
root.withdraw()

# 获取图片指定像素点的像素
def getPngPix(pngPath, pixelX=1, pixelY=1):
    img_src = Image.open(pngPath)
    img_src = img_src.convert('RGB')
    str_strlist = img_src.load()
    data = str_strlist[pixelX, pixelY]
    img_src.close()
    print(data)
    return data


if __name__ == '__main__':
    print("please wait few seconds...be patient...\n")
    # 选择一个图片文件
    Filepath = filedialog.askopenfilename()
    # Filepath = "tongliya1.jpg";
    print('Filepath:', Filepath)

    detect.detectPicture(Filepath);

    # 识别图片中的人脸并获取像素点
    img_path = "the_mouth.jpg"
    image_pixel = getPngPix(img_path)
    # print("image_pixel=", image_pixel)

    # 将像素点与数据集中的像素进行比较，选择最相似的一款并输出结果
    readJson.data_operate(image_pixel);
    os.system("pause");
