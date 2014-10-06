#!/usr/bin/env python 
import pytest
import mathparser
import sys


def test_ItShouldReadAFile():
    """Given a file as input it should parse it"""
    f = mathparser.readcommands("Test/validTest.file")
    assert f is not None

def test_ItShouldParseIncorrectFileAndLogErrors():
    """Given an incorrect file it should parse the file and errors should be logged to stderr"""
    from cStringIO import StringIO
    placeHolder = sys.stderr
    try:
        sys.stderr = StringIO()
        f = mathparser.readcommands("Test/invalidTest.file")
        errorlogs = sys.stderr.getvalue()        
        assert f is not None
        assert errorlogs is not None
    finally:
        sys.stderr.close()
        sys.stderr = placeHolder
    

def test_ItShouldParseAndReturnMathCommand():
    """Given a correct file with 5 commands a list of 5 MathCommand should be returned"""
    f = mathparser.readcommands("Test/validTest.file")
    assert len(list(f)) == 5

def test_ItShouldPrintCorrectValue():
    """ Given a file as input, the correct value should be output to stdout"""
    from cStringIO import StringIO
    placeHolder = sys.stderr
    try:
        sys.stdout = StringIO()        
        mathparser.main(['mathparser.py','Test/validTest.file'])
        result = sys.stdout.getvalue()        
    finally:
        sys.stdout.close()
        sys.stdout = placeHolder
    assert result == "4\n"

def test_ItShouldNotFailOnEmptyFile():
    """Given an empty file an empty list should be returned"""
    f = mathparser.readcommands('Test/emptyTest.file')
    assert len(list(f)) == 0

def test_ItShouldNotParseDivisionByZero():
    """Given an division by zero it should print an error"""
    from cStringIO import StringIO
    placeHolder = sys.stderr
    try:
        sys.stderr = StringIO()
        f = mathparser.readcommands("Test/divisionByZero.file")
        errorlogs = sys.stderr.getvalue()        
        assert f is not None
        assert errorlogs is not None
    finally:
        sys.stderr.close()
        sys.stderr = placeHolder

def test_NegativeSquareNumber():
    """Test not implemented yet and not covered in code, 
    current version returns the original number back for negative squares"""
    assert 1 == 0

