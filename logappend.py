#!/usr/bin/env python

import argparse
import db

# TODO: we should customize help output better
parser = argparse.ArgumentParser(description='Appends data to the log at the specified timestamp using the authentication token. If the log does not exist, logappend will create it. Otherwise it will append to the existing log. If the data to be appended to the log is not consistent with the current state of the log, logappend should print "invalid" and leave the state of the log unchanged.')

parser.add_argument('log', metavar='log',
                   help="The path to the file containing the event log. The log's filename may be specified with a string of alphanumeric characters. If the log does not exist, logappend should create it. logappend should add data to the log, preserving the history of the log such that queries from logread can be answered. If the log file cannot be created due to an invalid path, or any other error, logappend should print \"invalid\" and return -1.")

parser.add_argument('-T', dest='timestamp', action='store',
                   default=None, required=True,
                   help="Time the event is recorded. This timestamp is formatted as the number of seconds since the gallery opened and is a non-negative integer. Time should always increase, invoking logappend with an event at a time that is prior to the most recent event already recorded is an error.")

parser.add_argument('-K', dest='token', action='store',
                   default=None, required=True,
                   help="Token used to authenticate the log. This token consists of an arbitrary-sized string of alphanumeric (a-z, A-Z, and 0-9) characters. Once a log is created with a specific token, any subsequent appends to that log must use the same token.")

parser.add_argument('-E', dest='employee-name', action='store', default=None,
                   help="Name of employee. Names are alphabetic characters (a-z, A-Z) in upper and lower case. Names may not contain spaces.")

parser.add_argument('-G', dest='guest-name', action='store', default=None,
                   help="Name of guest. Names are alphabetic characters (a-z, A-Z) in upper and lower case. Names may not contain spaces.")

parser.add_argument('-A', dest='arrival', action='store_const', default=False, const=True,
                   help="Specify that the current event is an arrival; can be used with -E, -G, and -R. This option can be used to signify the arrival of an employee or guest to the gallery, or, to a specific room with -R. If -R is not provided, -A indicates an arrival to the gallery as a whole. No employee or guest should enter a room without first entering the gallery. No employee or guest should enter a room without having left a previous room. Violation of either of these conditions implies inconsistency with the current log state and should result in logappend exiting with an error condition.")

parser.add_argument('-L', dest='departure', action='store_const', default=False, const=True,
                   help="Specify that the current event is a departure, can be used with -E, -G, and -R.This option can be used to signify the departure of an employee or guest from the gallery, or, from a specific room with -R. If -R is not provided, -L indicates a deparature from the gallery as a whole. No employee or guest should leave the gallery without first leaving the last room they entered. No employee or guest should leave a room without entering it. Violation of either of these conditions implies inconsistency with the current log state and should result in logappend exiting with an error condition.")

parser.add_argument('-R', dest='room-id', action='store', default=None,
                   help="Specifies the room ID for an event. Room IDs are non-negative integer characters with no spaces. A gallery is composed of multiple rooms. A complete list of the rooms of the gallery is not available and rooms will only be described when an employee or guest enters or leaves one. A room cannot be left by an employee or guest unless that employee or guest has previously entered that room. An employee or guest may only occupy one room at a time. If a room ID is not specified, the event is for the entire art gallery.")

parser.add_argument('-B', dest='file', action='store', default=None,
                   help="Specifies a batch file of commands. file contains one or more command lines, not including the logappend command itself (just its options), separated by \n (newlines). These commands should be processed by logappend individually, in order. This allows logappend to add data to the file without forking or re-invoking. Of course, option -B cannot itself appear in one of these command lines. Commands specified in a batch file include the log name. Here is an example (the last one).")

args = parser.parse_args()

# TODO: handle error cases like -E and -G or -A and -L (we want xor!)
