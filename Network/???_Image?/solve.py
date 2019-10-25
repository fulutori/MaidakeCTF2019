import numpy as np
import os
from PIL import Image
import sys


def file2img(_file):
    arr = []
    arr = np.array(arr)
    with open(_file, 'rb') as f:
        while True:
            d = f.read(1)
            if len(d) == 0:
                break
            arr = np.append(arr,ord(d))
    arr = np.pad(arr,[0,256*int(arr.size/256+1)-arr.size],"constant")
    array = arr.reshape(-1,256)
    img = Image.fromarray(np.uint8(array))
    imgfile = "%s.png" % (_file)
    img.save(imgfile)

    return 0


def img2file(_file):
    img = np.array(Image.open(_file)).flatten()
    with open("output.pcap","wb") as f:
        for b in img:
            f.write(int(b).to_bytes(1,byteorder="big"))

    return 0


def main():
    argv = sys.argv
    argc = len(argv)
    if argc == 2:
        filename = argv[1]
        root,ext = os.path.splitext(filename)
        if ext == ".pcap":
            file2img(filename)
            sys.exit(0)
        elif ext == ".png":
            img2file(filename)
            sys.exit(0)
        else:
            print("Unexpected file")
            sys.exit(1)
    else:
        print("Usage: python3 %s filename" % argv[0])

    return 0



if __name__ == '__main__':
    main()
