import Constant as c
import argparse
import sys

class Arguments:
    def __init__(self):
        self.ap = argparse.ArgumentParser(description=c.PROG_DESC)
        self.ap.add_argument("-"+c.C_KEY, "--"+c.C_LONG_KEY, metavar=c.C_METAVAR, 
                            type=argparse.FileType(c.C_WR_TYPE), required=True, help=c.C_HELP)
        
    def getArgs(self):
        args = vars(self.ap.parse_args())
        return args[c.C_LONG_KEY]