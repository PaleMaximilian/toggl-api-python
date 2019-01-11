import APIRequest

import sys
from datetime import datetime
import moment
from argparse import ArgumentParser

_workspace_id = '3157122'
_api_token = '051ceec78370697e365af289363a70ac'
verified = True

parser = ArgumentParser(add_help=True)
parser.add_argument("--month", "-m", help="Enter the desired month")
parser.add_argument("--year", "-y", help="Enter the desired year (if no year is inputed, the current year is automatically used)")
parser.add_argument("--output", "-o", help="Enter the desired output file name")
args = parser.parse_args()
try:
    if args.month is None:
        month = raw_input("Enter the desired month: ")
    else:
        month = args.month

    if args.output is None:
        output = raw_input("Enter the output file name: ")
    else:
        output = args.output

    if args.year is None:
        year = moment.now().year
    else:
        year = args.year

    startdate = moment.date(month + " 1, " + str(year))
    enddate = moment.date(month + " 1, " + str(year)).add(months=1).subtract(days=1)
except Exception as e:
    verified = False
    print(e)

if(verified):
    APIRequest.requestData(_workspace_id,_api_token,startdate, enddate, year, output)
    print("Success")
else:
    print("Invalid option. Try --help for docs")
        

        



