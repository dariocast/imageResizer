#!/usr/bin/env python

import os, sys
from filecmp import cmp

from PIL import Image


def resizeImage(infile, output_dir="", size=(1024, 768)):
    outfile = os.path.splitext(infile)[0] + "_" + str(size[0]) + "x" + str(size[1])
    extension = os.path.splitext(infile)[1]

    if extension != '.PNG':
        return

    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(output_dir + '/' + outfile + extension, "JPEG")
        except IOError:
            print("cannot reduce image for ", infile)


if __name__ == "__main__":
    output_dir = "resized"
    dir = os.getcwd()

    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    for file in os.listdir(dir):
        resizeImage(file, output_dir, (1242, 2688))
        resizeImage(file, output_dir, (1242, 2208))
        resizeImage(file, output_dir, (2048, 2732))
