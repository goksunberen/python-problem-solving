import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh = s[0:2]
    if s.endswith("PM" or "pm") and hh != "12":
        hh = int(hh) + 12
        return str(hh) + s[2:8]
    if s.endswith("AM" or "am") and hh == "12":
        hh = "00"
        return str(hh) + s[2:8]
    if s.endswith("PM" or "pm") and hh == "12":
        return str(hh) + s[2:8]
    else:
        return s[0:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
