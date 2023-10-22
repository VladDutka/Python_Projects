import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder
def main():
    P = int(sys.argv[1])        # Minimum blob size
    tau = float(sys.argv[2])    # Luminance threshold
    delta = float(sys.argv[3])  # Maximum displacement
    files = sys.argv[4:]        # List of images to check.

    # Get list of beads in initial frame. This will become beads0 on the first
    # iteration of the loop.
    beads1 = BlobFinder(Picture(files[0]), tau).getBeads(P)

    # Loopt through rest of file list.
    for i in range(1, len(files)):
        # The first frame is the second frame of the last iteration:
        beads0 = beads1
        # The second frame is the next one in the list:
        beads1 = BlobFinder(Picture(files[i]), tau).getBeads(P)

        # Loop through the bead list to find out how far each one moved
        for bead in beads1:
            # Find the distance to the closest bead in beads1
            dist = min(bead.distanceTo(other) for other in beads0)
            # If the distance is less than the maximum distance considered,
            # it is assumed to be the same blob
            # and the distance is written to the terminal
            if dist <= delta:
                stdio.writef('%.4f\n', dist)
        stdio.writeln()


if __name__ == '__main__':
    main()
