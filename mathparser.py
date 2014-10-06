#!/usr/bin/env python 
"""
Reads a file parsing the commands returns the result of the equation
Usage is mathparser.py [-h] file
"""

import os
import sys
import math
import getopt

class OperatorBase(object):   
    def load(self, value):
        self.value = int(value)

    def apply(self,value):
        return value

class SingleOperator(OperatorBase):
    def valid(self):
        return True

class SquareRootOperator(SingleOperator):
    def apply(self,value):
        return math.sqrt(value)

class IntegerSquareRootOperator(SquareRootOperator):
    #Newtons method
    def apply(self,value):
        x = value
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + value // x) // 2
        return x

class TwoComponentOperator(OperatorBase):
    def valid(self):
        return self.value is not None and isinstance(self.value, (int) )

class AddOperator(TwoComponentOperator):    
    def apply(self,value):
        return value + self.value

class MultiplyOperator(TwoComponentOperator):
    def apply(self,value):
        return value * self.value

class DivisionOperator(TwoComponentOperator):
    def apply(self,value):
        return value // self.value
    
    def valid(self):
        return self.value != 0

class SubtractionOperator(TwoComponentOperator):
    def apply(self,value):
        return value - self.value


class MathOperatorFactory:
    def parse(self,line):
        values = line.split()
        length = len(values)
        #Cant you splat in python?
        if length < 1:
            print >>sys.stderr, "Empty row found in input file"
            return None
        if values[0] not in self.operators:
            print >>sys.stderr, "{} is not in list of recognized commands {}".format(values[0], self.operators.keys())
            return None
        operator = self.operators[values[0]]()
        if length >= 2 :
            operator.load(values[1])
        if not operator.valid():
            print >>sys.stderr, "command {} value {} is not a valid combination".format(values[0],values[1])
            return None
        return operator

    operators = {
            "ADD" : AddOperator,
            "MUL" : MultiplyOperator,
            "DIV" : DivisionOperator,
            "SUB" : SubtractionOperator,
            "SQR" : IntegerSquareRootOperator
        }

def readcommands(file):
    with open(file, "r") as fileHandler:
        factory = MathOperatorFactory();
        return filter(None,(factory.parse(line) for line in fileHandler))

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

#Reading up guide lines for main according to Russo
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        scans = 5
        delay = 0
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                sys.exit(0)

        commands = readcommands(args[0])

        result = reduce(lambda total, current : current.apply(total), commands, 0)
        print result

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
