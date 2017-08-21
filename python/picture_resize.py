import argparse
import os
import PIL
from PIL import Image

WIDTH = 200
HEIGHT = 200


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--from", action="store", dest="from_filename",
                        required=True,
                        help="Filename of the input file for thumbnail")
    parser.add_argument("-t", "--to", action="store", dest="to_filename",
                        required=False, default=None,
                        help="Filename of the output file for thumbnail")
    parser.add_argument("-x", "--width", action="store", type=int, dest="width",
                        required=False, default=WIDTH,
                        help="Resize to width")
    parser.add_argument("-y", "--height", action="store", type=int, dest="height",
                        required=False, default=HEIGHT,
                        help="Resize to height")

    known, others = parser.parse_known_args()
    from_filename = os.path.abspath(known.from_filename)
    if known.to_filename is None:
        to_filename = os.path.join(
            os.path.dirname(from_filename),
            "thumbnail_" + os.path.basename(from_filename))
    else:
        to_filename = os.path.abspath(known.to_filename)

    img = Image.open(from_filename)
    resizex = float(known.width) / float(img.size[0])
    resizey = float(known.height) / float(img.size[1])

    if resizex < resizey:
        wsize = known.width
        hsize = int((float(img.size[1]) * float(resizex)))
    else:
        wsize = int((float(img.size[0]) * float(resizey)))
        hsize = known.height

    print("Resizing image from {0} {1}x{2} to {3} {4}x{5}".format(
        from_filename, img.size[0], img.size[1], to_filename, wsize, hsize))

    img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
    img.save(to_filename)

if __name__ == "__main__":
    main()
