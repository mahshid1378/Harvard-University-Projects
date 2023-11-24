import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    hourstart = 0
    minstart = 0
    hourend = 0
    minend = 0
    meridianstart = ""
    meridianend = ""


    if twelvehour := re.search(r"^([1-9]|1[0-2]):?([0-5][0-9])?(?: )(AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])?(?: )(AM|PM)$", s, re.IGNORECASE):
        hourstart = twelvehour.group(1)
        if twelvehour.group(2) == None:
            minstart = 0
        else:
            minstart = twelvehour.group(2)
        meridianstart = twelvehour.group(3)
        hourend = twelvehour.group(4)
        if twelvehour.group(5) == None:
            minend = 0
        else:
            minend = twelvehour.group(5)
        meridianend = twelvehour.group(6)

    else:
        raise ValueError

    hourstart = int(hourstart)
    minstart = int(minstart)
    hourend = int(hourend)
    minend = int(minend)

    return f"{startconvert(hourstart, meridianstart):02}:{minstart:02} to {endconvert(hourend, meridianend):02}:{minend:02}"

def startconvert(hourstart, meridianstart):

    if meridianstart.upper() == "AM":
        if hourstart == 12:
            beg_hour = 0
        else:
            beg_hour = hourstart
    else:
        if hourstart == 12:
            beg_hour = hourstart
        else:
            beg_hour = hourstart + 12

    return beg_hour

def endconvert(hourend, meridianend):

    if meridianend.upper() == "AM":
        if hourend == 12:
            end_hour = 0
        else:
            end_hour = hourend
    else:
        if hourend == 12:
            end_hour = hourend
        else:
            end_hour = hourend + 12

    return end_hour

if __name__ == "__main__":
    main()