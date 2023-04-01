import pytest

def test_valid_login():
    print("valid login!!")

def test_invalid():
    print("invalid")
    actual_title=''
    assert actual_title=='OrangeHRM'
    assert 'Orange' in actual_title