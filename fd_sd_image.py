import numpy as np
import cv2
from PIL import Image

def minus(lst1, lst2, scalar):
    ans = []
    for i in range(len(lst1)):
        a = (int(lst1[i]) - int(lst2[i])) / scalar
        if a < 0:
            a += 255
        elif a > 255:
            a -= 255

        ans.append(a)
    return ans

def y_derivative(matrix):
    ans = []

    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        lst = []
        for j in range(m):
            lst.append(0.)
        ans.append(lst)
    for i in range(n):
        for j in range(m):
            if i == 0:
                ans[i][j] = minus(matrix[i + 1][j], matrix[i][j], 1)
            elif i == n - 1:
                ans[i][j] = minus(matrix[i][j], matrix[i - 1][j], 1)
            else:
                ans[i][j] = minus(matrix[i + 1][j], matrix[i - 1][j], 2)

    return ans


def x_derivative(matrix):
    ans = []

    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        lst = []
        for j in range(m):
            lst.append(0.)
        ans.append(lst)

    for j in range(m):
        for i in range(n):
            if j == 0:
                ans[i][j] = minus(matrix[i][j + 1], matrix[i][j], 1)
            elif j == m - 1:
                ans[i][j] = minus(matrix[i][j], matrix[i][j - 1], 1)
            else:
                ans[i][j] = minus(matrix[i][j + 1], matrix[i][j - 1], 2)

    return ans

def first_order_derivative(matrix):
    x = x_derivative(matrix)
    y = y_derivative(matrix)
    return [x, y]


def second_order_derivative(matrix):
    x = x_derivative(matrix)
    y = y_derivative(matrix)
    xy = y_derivative(x)
    return [x, y, xy]

def convert_to_image(arr):
    convert = np.array(arr)
    img = Image.fromarray((convert * 255).astype(np.uint8))
    img.show()

print("please enter the path: ")
img = input()
image = cv2.imread(img)
arr = np.array(image)

print("please wait, it needs some seconds")
print("this is the first derivative: ")
print(first_order_derivative(arr))

print("please wait, it needs some seconds")
print("this is the second derivative: ")
print(second_order_derivative(arr))

print("these are pixels of images, I didn't converted into image back beacuse in this way it's easier to test")
print("if you want to test on images I have convert_to_image() function for it")
