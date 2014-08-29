#!/usr/bin/env python

import argparse
import db

# TODO: we should customize help output better
parser = argparse.ArgumentParser(description='queries the state of the gallery. It prints which employees and guests are in the gallery or its rooms, and allows for various time-based queries of the state of the gallery.')

parser.add_argument('log', metavar='log',
                   help="The path to the file log used for recording events. The filename may be specified with a string of alphanumeric characters.")

parser.add_argument('-K', dest='token', action='store',
                   default=None, required=True,
                   help="Token used to authenticate the log. This token consists of an arbitrary sized string of alphanumeric characters and will be the same between executions of logappend and logread. If the log cannot be authenticated with the token (i.e., it is not the same token that was used to create the file), then \"security error\" should be printed to stderr and -1 should be returned.")

parser.add_argument('-E', dest='employee-name', action='store', default=None,
                   help="Employee name. May be specified multiple times.")

parser.add_argument('-G', dest='guest-name', action='store', default=None,
                   help="Guest name. May be specified multiple times.")

parser.add_argument('-H', dest='html', action='store_const', default=False, const=True,
                   help="Specifies output to be in HTML (as opposed to plain text). Details in options below.")

parser.add_argument('-S', dest='state', action='store_const', default=False, const=True,
                   help="Print the current state of the log to stdout. The state should be printed to stdout on at least two lines, with lines separated by the \n (newline) character. The first line should be a comma-separated list of employees currently in the gallery. The second line should be a comma-separated list of guests currently in the gallery. The remaining lines should provide room-by-room information indicating which guest or employee is in which room. Each line should begin with a room ID, printed as a decimal integer, followed by a colon, followed by a space, followed by a comma-separated list of guests and employees. Room IDs should be printed in ascending integer order, all guest/employee names should be printed in ascending lexicographic string order. If -H is specified, the output should instead be formatted as HTML conforming to the following HTML specification.")

parser.add_argument('-R', dest='roomlist', action='store_const', default=False, const=True,
                   help="Give a list of all rooms entered by an employee or guest. Output the list of rooms in chronological order. If this argument is specified, either -E or -G must be specified. The list is printed to stdout in one comma-separated list of room identifiers. If -H is specified, the format should instead by in HTML conforming to the following HTML specification.")

args = parser.parse_args()

# TODO: add all the optional arguments (commented out until implemented?)

# TODO: handle error cases, -R and -S, -R without -E or -G (or both!) ... see the spec!
