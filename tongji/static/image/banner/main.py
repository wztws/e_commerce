from PIL import Image

image1 = Image.open('02.png')

# 打开图片02.png

# 调整01.png的大小为02.png的大小
resized_image = image1.resize((1200, 800))

# 保存调整后的图片为result.png
resized_image.save('result.png')

# 关闭图片
image1.close()
