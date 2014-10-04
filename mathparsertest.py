import pytest
import mathparser




def test_ItShouldReadAFile():
    f = mathparser.readcommands("Test/validTest.file")
    assert f is not None

def test_ItShouldParseIncorrectFileAndLogErrors():
    f = mathparser.readcommands("Test/invalidTest.file")
    assert f is not None
    #Make sure incorrect file is logged here.

def test_ItShouldParseAndReturnMathCommand():
    f = mathparser.readcommands("Test/validTest.file")
    assert len(list(f)) == 5
    #Make sure incorrect file is logged here.
