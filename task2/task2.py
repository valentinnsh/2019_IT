import matplotlib.pyplot as plt
import numpy as np
import math


def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return


def get_gauss_kernel(windos_size, sig):
    kernel = np.zeros((windos_size, windos_size))
    s2 = 2*sig**2
    ad = math.floor(windos_size/2)
    for x in [-ad, ad]:
        for y in [-ad, ad]:
            numer = np.sqrt(x**2+y**2)
            kernel[x+ad, y+ad] = (
                np.exp(-(numer**2/s2))/s2/np.pi)

    kernel /= kernel.sum()  # normalise
    return kernel


def filter(img, window_size=3, sig=1):
    img2 = np.zeros_like(img)
    kernel = get_gauss_kernel(window_size, sig)
    p = window_size//2
    for k in range(img.shape[2]):  # foreach color channel
        for i in range(p, img.shape[0]-p):  # foreach row
            for j in range(p, img.shape[1]-p):  # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i, j, k] = (kernel*window).sum()
    return img2


def main():
    img = plt.imread("tick.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img, 3, 1)

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()
