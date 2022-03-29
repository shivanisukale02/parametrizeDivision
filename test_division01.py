import division01
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False)])
def test_div5(num,output):
    result=division01.div5(num)
    assert result==True

def test_div7():
    a = 14
    result = division01.div7(a)
    assert result == True

def test_div9():
    a = 18
    result = division01.div9(a)
    assert result == True

def test_div11():
    a = 22
    result = division01.div11(a)
    assert result == True
