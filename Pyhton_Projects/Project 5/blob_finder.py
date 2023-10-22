import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic,
    # using a luminance threshold tau.
    def __init__(self, pic, tau):
        # Initialize an empty list for the blobs in pic.
        self._blobs = []
        # Create a 2D list of booleans called marked, having the same
        # dimensions as pic.
        marked = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call self._findBlob() with the right arguments.
        # 3. Add blob to self.blobs if it has a non-zero mass.
        for i in range(pic.width()):
            for j in range(pic.height()):
                if luminance.luminance(pic.get(i, j)) > tau:
                    blob = Blob()  # creates a Blob object
                    self._findBlob(pic, tau, i, j, marked, blob)
                    if blob.mass() > 0:  # if mass of blob is greater than 0
                        self._blobs += [blob]  # appending blob to self blobs

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        a = []  # creating an empty list for variable a
        b = len(self._blobs)  # length of self._blobs
        for i in range(b):
            if self._blobs[i].mass() >= pixels:  # if mass of the blob is
                # greater than or equal to pixels

                a += [self._blobs[i]]  # appending self._blobs to variable
        return a

    # Identifies a blob using depth-first search. The parameters are the
    # picture (pic), luminance threshold (tau), pixel column (i), pixel
    # row (j), 2D boolean matrix (marked), and the blob being identified (blob)
    def _findBlob(self, pic, tau, i, j, marked, blob):

        # Base case: return if pixel (i, j) is out of bounds, or
        # if it is marked, or if its luminance is less than tau.
        if i < 0 or i >= pic.width():  # return if pixel i is out of bounds
            return
        if j < 0 or j >= pic.height():  # return if pixel j is out of bounds
            return
        if marked[i][j]:  # return if pixel is marked
            return
        if luminance.luminance(pic.get(i, j)) < tau:  # if luminance is less
            # than tau
            return

        # Mark the pixel.
        marked[i][j] = True  # marked the pixel as True

        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call self._findBlob() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i + 1, j, marked, blob)   # South
        self._findBlob(pic, tau, i - 1, j, marked, blob)   # North
        self._findBlob(pic, tau, i, j + 1, marked, blob)   # East
        self._findBlob(pic, tau, i, j - 1, marked, blob)  # West


# Unit tests the data type (DO NOT EDIT).
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef('%d Beads:\n', len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef('%d Blobs:\n', len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == '__main__':
    _main()
