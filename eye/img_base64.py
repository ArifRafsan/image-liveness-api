import base64

def img_base64():
    path = "media/videos/"
    image = open(path + 'gg.mp4.jpg', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)

    return image_64_encode

#print(img_base64())