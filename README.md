# EXIFExport
Produces barcharts and historgrams with frequency of time of day the pictures in your directory were taken.

This program itertates through either your folder or a folder of folders containing .JPG images
and reads the exif data and sums it to give you a barchart or historgram of what hour of the day the
images were taken.

It was originally developed to aid a deer population survey by counting the shutters of trail cameras.

# Future development
* Comment code
* Non-jpg case handling
* Get rid of globals, case switch and independent hour update functions and pass arrays instead
