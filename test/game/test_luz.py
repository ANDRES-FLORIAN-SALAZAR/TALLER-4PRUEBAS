import pytest
from lucesfuera.game.luz import Luz

def test_luz_enum_values():
    assert Luz.OFF.name == "OFF"
    assert Luz.ON.name == "ON"

def test_luz_enum_auto_values():
    assert Luz.OFF.value == 1
    assert Luz.ON.value == 2