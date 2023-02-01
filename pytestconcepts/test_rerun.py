import pytest

def test_methodone():
    var1=1
    var2=2
    assert var1==var2

# pytest --reruns 5 --reruns-delay 1 test_rerun.py
