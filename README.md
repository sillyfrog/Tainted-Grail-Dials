# Tainted Grail Dials

Source code for a 3D printed Tainted Grail Dials. These have been designed to provide better contrast and readability of the numbers.

See the built files here: https://www.thingiverse.com/thing:4839257

I used 2 colors, changing at 0.46mm and back again at 1.9mm.

## Development Notes

The Skull portion is based on the Celtic Skull by artec3d available here: https://www.thingiverse.com/thing:29114

This is built using SolidPython, which will then output a `dial.scad` and `dial_skull.scad` - these should be compiled to make 2 .stl files, that can then be combined to make the final object. I needed to do this as OpenSCAD crashed when trying to compile it all as one. You can combine them in your slicer (in Cura, select both parts, right click and select "Merge Models").

To generate a single file, I used Meshmixer (for upload to thingiverse).

Enjoy!
