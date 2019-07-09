# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/9 22:44'

row, col, min_p, max_p, replace_p = input().split()
for i in range(int(row)):
    pixels = input().split()
    for j, pixel in enumerate(pixels):
        if int(pixel) <= int(max_p) and int(pixel) >= int(min_p):
            pixels[j] = replace_p
    print(' '.join([i.zfill(3) for i in pixels]))