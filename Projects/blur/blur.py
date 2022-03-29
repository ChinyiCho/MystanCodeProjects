"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: 來自old_img
    :return: 經一次blur處理的圖
    """
    new_w = img.width
    new_h = img.height
    new_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            n_img_p = new_img.get_pixel(x, y)
            num = 0
            sum_r = 0
            sum_g = 0
            sum_b = 0
            for i in range(3):
                if x - 1 + i < 0 or x - 1 + i > img.width - 1:
                    pass
                else:
                    for j in range(3):
                        if y - 1 + j < 0 or y - 1 + j > img.height - 1:
                            pass
                        else:
                            num += 1
                            img_ij = img.get_pixel(x - 1 + i, y - 1 + j)
                            sum_r += img_ij.red
                            sum_g += img_ij.green
                            sum_b += img_ij.blue
            n_img_p.red = sum_r // num
            n_img_p.green = sum_g // num
            n_img_p.blue = sum_b // num
    return new_img


def main():
    """
    TODO: 經n次blur處理的圖
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
