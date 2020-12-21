import cv2 as cv
import numpy as np


#  一维数组操作
def twinlinearrorate(img, w, h, sita, xr, yr):
    img=img.reshape(img.shape[0]*img.shape[1], )
    new=np.zeros(img.shape[0])

    nsita = -sita * np.pi / 180
    sinsita = np.sin(nsita)
    cossita = np.cos(nsita)
    for y in range(0, h):
        for x in range(0, w):
            tx = (x - xr) * cossita - (y - yr) * sinsita + xr
            ty = (y - yr) * cossita + (x - xr) * sinsita + yr
            ix = np.ceil(tx).astype(np.int)
            iy = np.ceil(ty).astype(np.int)
            if (ix < 0) | (ix > w - 2) | (iy < 0) | (iy > h - 2):
                continue

            p1 = img[iy * w + ix]
            p2 = img[iy * w + ix]

            p3 = img[iy * w + ix]
            p4 = img[iy * w + ix]
            p12 = p1 + (tx - ix) * (p2 - p1)
            p34 = p3 + (tx - ix) * (p4 - p3)

            new[y*w+x] = p12 + (ty - iy) * (p34 - p12)

    cv.imwrite("onedim.jpg", new.reshape(h, w))


if __name__ == '__main__':
    img = cv.imread("1.jpg", cv.IMREAD_GRAYSCALE)
    h, w = img.shape[:2]
    print("图片宽高?:", h, w)
    angle = 30
    twinlinearrorate(img, w, h, angle, 70, 70)


