# MasterSegmenter

In order to use this code you might need to install some necessary python packages like
* PyQt5
* scikit-skimage
* pyclesperanto
* colorcet

This is a Graphical User Interface (GUI) that takes .tiff pictures of beads/nuclei/particles, segments it and returns a labelled picture, where each pixel value represents a single object.
It can be launched from the terminal in the root folder, with 'python MasterSegmenter_GUI.py'
There are four user-input parameters:

* BG noise: size (in pixel) of a square-box kernel used to smooth out background noise and small signals
* Threshold: a hard pixel-value threshold performed on the image before resuming the analysis. This can get rid of e.g. weak fluorescence signals
* Sigma-Spot: expected size of the blobs to be detected
* Sigma-Outline: tightness of the segmentation around the object. If volume measurements are important, a value of 1 is recommended, since higher values can artificially inflate the volume.

  The user is able to load a .tif/.tiff image from the menu File...--> Open TIFF and play around with the segmentation parameters until a satisfactory segmentation is achieved.
  Once optimal parameters have been found, the button "Segment folder" performs the same analysis on all images available in the folder, ans saves two outputs per input:
  * A labelled .tif, where each pixel value corresponds to a detected object (8-bit or 16-bit, depending on the amount of beads)
  * A .txt file with the estimated radius of each particle (assuming 1um isotropic resolution and round objects)
  


