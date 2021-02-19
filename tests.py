#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 19

def test_code():
    assert main.list10([0,0,0,0,0,0]) == False, "list10([0,0,0,0,0,0]) == False FAILED"
    assert main.list10([0,0,0,0,0,0,0,0,0,0,0,0,10]) == True, "list10([0,0,0,0,0,0,0,0,0,0,0,0,10]) == True FAILED"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
