from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series



def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_negative():
    expect=fibonacci(-1)
    actual="negative num"
    assert expect==actual

def test_fibonacci_zero():
    expect=fibonacci(0)
    actual=0
    assert expect==actual

def test_fibonacci_one():
    expect=fibonacci(1)
    actual=1
    assert expect==actual

def test_fibonacci_five():
    expect=fibonacci(5)
    actual=5
    assert expect==actual

def test_lucas_negative():
    expect=lucas(-1)
    actual="negative num"
    assert expect==actual

def test_lucas_zero():
    expect=lucas(0)
    actual=2
    assert expect==actual

def test_lucas_one():
    expect=lucas(1)
    actual=1
    assert expect==actual

def test_lucas_five():
    expect=lucas(5)
    actual=11
    assert expect==actual


def test_sum_series_negative():
    expect=sum_series(-1)
    actual="negative num"
    assert expect==actual

def test_sum_series_zero():
    expect=sum_series(0)
    actual=0
    assert expect==actual

def test_sum_series_one():
    expect=sum_series(1)
    actual=1
    assert expect==actual

def test_sum_series_five():
    expect=sum_series(5)
    actual=5
    assert expect==actual

def test_sum_series_threeparam():
    expect=sum_series(1,1,2)
    actual=2
    assert expect==actual
