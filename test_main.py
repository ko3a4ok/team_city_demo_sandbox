__author__ = 'ko3a4ok'
import main


def test_fn1():
    return main.power2(4) == 4*4


def test_fn2():
    try:
        main.power2(range(10))
        assert False
    except TypeError:
        assert True


def test_failed():
    assert main.power2(3) == 10