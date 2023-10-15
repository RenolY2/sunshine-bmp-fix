# sunshine-bmp-fix
Script to fix BMPs for use with Super Mario Sunshine's BMP.
Has been tested with 8-bit BMPs created by Paint.net 5.0.9

Usage: Drag 8-bit BMP onto fixbmp.bat. The BMP will be fixed in place. 

Command line usage: ``python bmpfix.py <path to bmp>``

Technical explanation: Super Mario Sunshine expects 8-bit BMPs with a full 256 color palette ranging from 0 to 255 in order of the greyscale values, so that the indicies into the palette for each pixel are consistent with the greyscale value. Many image editing programs save an 8-bit BMP with the colors out of order or the palette being incomplete, requiring the BMP to be fixed for Sunshine use or the goop drawing will broken ingame.
