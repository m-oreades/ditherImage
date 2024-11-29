This script converts an image to a dithered version, hopefully eliminating large areas or lines of solid color.

Resolution is ok above 200 pixels wide. Details really begin to degrade when the image width is less than 100 pixels.

Intended application:
to convert an image with gradient to a two color pattern suitable for knitting. The dithering attempts to eliminate continuous runs of any color, preventing hanging yarns on the reverse side.
This approach is suitable for larger scale patterns, possibly for a sweater, or a tube knit with very small gauge needles.

Notable issues:
In smaller resolution images with high frequency content, there is an issue where the horizontal rows sometimes exceed 7 consecutive pixels of the same color as many as 9 consecutive pixels have been observed so far. This is an artifact of how the image processing works. for smaller, high frequency images, a different dithering method is probably needed to get good results.
a possible workaround would be to reduce the contrast of the image.