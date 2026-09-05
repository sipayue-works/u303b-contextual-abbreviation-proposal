#!/usr/bin/env python3
"""
Build a one-glyph OpenType/TrueType test font for U+303B from u303b_variant_glyph.svg.

Requires FontForge with Python support.
Run:
    fontforge -script build_u303b_variant_font.py

IMPORTANT:
- This maps the supplied glyph to the EXISTING character U+303B.
- It does NOT create a new Unicode code point.
- Edit the ownership/license fields below before building.
"""

import fontforge
import os
import sys

SVG = os.path.join(os.path.dirname(__file__), "u303b_variant_glyph.svg")
OUTPUT = os.path.join(os.path.dirname(__file__), "U303BContextualVariant.ttf")

FAMILY = "U303B Contextual Variant"
FONTNAME = "U303BContextualVariant-Regular"
FULLNAME = "U303B Contextual Variant Regular"

COPYRIGHT_NOTICE = "REPLACE WITH COPYRIGHT / OWNERSHIP NOTICE"
MANUFACTURER = "REPLACE WITH FONT OWNER OR MANUFACTURER"
DESIGNER = "REPLACE WITH GLYPH / FONT DESIGNER"
LICENSE_DESCRIPTION = "REPLACE WITH AN ACCEPTABLE LICENSE, e.g. SIL Open Font License 1.1 (OFL-1.1)"
LICENSE_URL = "REPLACE WITH LICENSE URL IF APPLICABLE"

required = [COPYRIGHT_NOTICE, MANUFACTURER, DESIGNER, LICENSE_DESCRIPTION]
if any(v.startswith("REPLACE") for v in required):
    sys.exit("Edit the ownership and license fields at the top of the script before building.")

font = fontforge.font()
font.encoding = "UnicodeFull"
font.em = 1000
font.ascent = 880
font.descent = 120
font.familyname = FAMILY
font.fontname = FONTNAME
font.fullname = FULLNAME
font.weight = "Regular"

g = font.createChar(0x303B, "uni303B")
g.importOutlines(SVG)
g.width = 1000

# Center the outline inside the advance width.
xmin, ymin, xmax, ymax = g.boundingBox()
dx = (1000 - (xmax - xmin)) / 2 - xmin
g.transform((1, 0, 0, 1, dx, 0))

# OpenType name table information relevant to Unicode font submission.
font.appendSFNTName("English (US)", "Copyright", COPYRIGHT_NOTICE)
font.appendSFNTName("English (US)", "Manufacturer", MANUFACTURER)
font.appendSFNTName("English (US)", "Designer", DESIGNER)
font.appendSFNTName("English (US)", "License", LICENSE_DESCRIPTION)
if LICENSE_URL and not LICENSE_URL.startswith("REPLACE"):
    font.appendSFNTName("English (US)", "License URL", LICENSE_URL)

# Generate the font locally.
font.generate(OUTPUT)
font.close()

print("Built:", OUTPUT)
print("Character mapping: U+303B VERTICAL IDEOGRAPHIC ITERATION MARK")
