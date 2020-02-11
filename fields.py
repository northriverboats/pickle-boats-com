#!/usr/bin/env python

"""
Notes:
  * Page is divide into 3 types of bands: top, bottom, and section(s)
  * If a column is CALCULATED it is column + (index into boatSection * 4)
  * If a row is OFFSET it is offset + row
  * These are done with sections[], boatSizes[] start[], end[]
    * sections[] the order the sections are to be found in on the sheet
    * boatSizes[] the boat lengths are integers found in Row 1
    * start[] of each section where "QTY" found in Column A (1)
    * end[] of each section where "SUBTOTAL " found in Column J (10)
  * To process a sheet the a dictionary entry is made with the key being
    the name of boat model and the value is another dictionary.
  * Examples use the Seahawk Outboard for Boat Model:
    * Top/Bottom directly addressed: ['Seahawk Outboard']['OVERHEAD BOAT']
    * Section top/bottom directly addressed: ['Seahawk Outboard']['TRAILER LABOR RATE']
    * Section parts list is an array found in: ['Seahawk Outboard']['TRAILER PARTS']
    * Section parts are referenced by index: ['Seahawk Outboard']['TRAILER PARTS'][0]
    * Parts details are addressed: ['Seahawk Outboard']['TRAILER PARTS'][0]['UOM']
"""

start = 10
end = 12
width = 4

# order of sections corresponds with order of starts and ends
sections = [
    "TRAILER",
    "ENGINE & JET",
    "FABRICATION",
    "CANVAS",
    "PAINT",
    "OUTFITTING"
]

possibleSize = [
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57
]

##  TOP BAND        #########################################################

# top of sheet, absolute row, absolute column - not by boat size
# [0] title, [1] column, [2] row, [3] default
topSection = [
    ["BOAT MODEL", 1, 1, ""],
    ["OVERHEAD BOAT", 6, 5, ""],
    ["RETAIL BOAT", 5, 6, ""],
    ["OVERHEAD MOTOR AND TRAILER", 6, 7, "0"],
    ["RETAIL MOTOR AND TRAILER", 5, 8, "0"],
]    

# top of sheet, calculated column, absolute row - by boat size
# [0] title, [1] column, [2] row, [3] default
costSummary = [
    [" LABOR TOTAL", 13, 2, "0"],
    [" MATERIAL TOTAL", 13, 3, "0"],
    [" TRAILER / ENGINE & JET", 13, 4, "0"],
    [" TOTAL COST", 13, 5, "0"],
	[" RETAIL BASE BOAT", 13, 6, "0"],
	[" RETAIL MOTOR / TRAILER", 13, 7, "0"],
	[" CALCULATED RETAIL TOTAL", 13, 8, "0"],
	[" CALCULATED DEALER INVOICE", 13, 9, "0"],
	[" CALCULATED CM", 13, 10, "0"],
	[" ADVERTISED RETAIL TOTAL", 13, 12, "0"],
	[" ADVERTISED DEALER INVOICE", 13, 13, "0"],
	[" ADVERTISED CM", 13, 14, "0"],
]

boatLength = [
	["BOAT SIZE", 10, 1, ""],
]

##  BOTTOM BAND    ##########################################################

# bottom section - max(end) + 5, absolute column, offest row - not by boat size
# [0] title, [1] column, [2] row, [3] default
bottomSection = [
]


##  SECTION BANDS  ##########################################################

# top of section, absolute column, offset row - not by boat size
# [0] title, [1] column, [2] row, [3] default
startSections = [
    [" CONSUMABLES", 4, -1, "0"],
    [" LABOR RATE", 6, -1, "0"],
]

# top of section, calculated column, offset row - by boat size
# [0] title, [1] column, [2] row, [3] default
startSectionsSize = [
    [" HOURS", 12, -1, "0"]
]

# bottom of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
endSections = [
    [" SUBTOTAL ALL", 13, 0, "0"],
    [" CONSUMABLES", 13, 1, "0"],
    [" TOTAL", 13, 2, "0"],
]

# 1/2 body of section, absolute column, offset row
# [0] title, [1] column, [2] row, [3] default
partSection = [
    ["PART NUMBER", 4, 1, ""],
    ["DESCRIPTION", 5, 1, ""],
    ["UOM", 6, 1, ""],
    ["PRICE", 7, 1, "0"],
    ["VENDOR", 8, 1, ""],
    ["VENDOR PART", 10, 1, ""],
]

# 2/2 body of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
partSectionByModel = [
    [" QTY", 10, 1, "0"],
    [" TOTAL", 13, 1, "0"], 
]