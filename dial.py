#!/usr/bin/env python3
from solid import *
from solid.utils import *
import pathlib
import math

use("Grail.scad")

WIDTH = 30
QTRW = WIDTH / (1 + sqrt(2)) / 2
HLFW = WIDTH / 2

BASE_H = 1.8

LOW_H = 0.4
HIGH_H = LOW_H + 0.6


def octogon(width):
    qtrw = width / (1 + sqrt(2)) / 2
    hlfw = width / 2
    return polygon(
        [
            [-qtrw, hlfw],
            [qtrw, hlfw],
            [hlfw, qtrw],
            [hlfw, -qtrw],
            [qtrw, -hlfw],
            [-qtrw, -hlfw],
            [-hlfw, -qtrw],
            [-hlfw, qtrw],
        ]
    )


def numbers(h):
    ret = []
    for i in range(8):
        ret.append(
            rotate([0, 0, i * 45])(
                translate([0, -14, 0])(
                    linear_extrude(h)(
                        text(
                            str(i + 1),
                            size=4.8,
                            # font="Gloucester MT Extra Condensed:style=Bold",
                            # font="Times New Roman:style=Bold",
                            # font="Arial Rounded MT Bold:style=Regular",
                            font="Arial Black:style=Regular",
                            # valign="center",
                            halign="center",
                        )
                    )
                )
            )
        )
    return sum(ret)


def main():
    o = linear_extrude(BASE_H + LOW_H)(octogon(WIDTH)) - up(BASE_H)(
        linear_extrude(BASE_H)(octogon(WIDTH - 1.5))
    )
    o += cylinder(d=WIDTH, h=BASE_H + LOW_H) - cylinder(d=WIDTH - 1, h=BASE_H + 6)
    o += cylinder(d=18, h=BASE_H + HIGH_H) - cylinder(d=18 - 0.8, h=BASE_H + 6)

    o += up(BASE_H)(numbers(LOW_H))

    # Back, make it all 1mm high, then hove down to cutout level
    back = translate([0, -0.5, 0])(scale([0.08, 0.08, 1])(Grail(1)))
    # back += cylinder(d=WIDTH, h=1) - down(0.1)(cylinder(d=WIDTH - 1, h=BASE_H + 6))
    back += cylinder(d=18, h=1) - down(0.1)(cylinder(d=16.2, h=BASE_H + 6))
    back += numbers(1)

    o -= up(0.4)(rotate([0, 180, 0])(back))

    dial_skull = translate([0, -3.5, BASE_H])(
        scale([1, 1, 0.4])(import_stl("flat_skull.stl"))
    )
    dial_skull -= translate([0, 0, BASE_H + HIGH_H])(cylinder(d=WIDTH, h=10))
    # o += dial_skull

    saveasscad(o, "dial", 100)
    saveasscad(dial_skull, "dial_skull", 10)


def saveasscad(obj, desc, fn=50):
    pfn = pathlib.Path(__file__)
    outfn = pfn.parent / ("{}.scad".format(desc))
    scad_render_to_file(obj, outfn, file_header=f"$fn = {fn};\n")


if __name__ == "__main__":
    main()
