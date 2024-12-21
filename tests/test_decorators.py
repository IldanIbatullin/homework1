import pytest
from decorators import log

@log("logs/test_log.txt")
def test_function(x, y):
    return x + y

def test_log_success(capfd):
    result = test_function(3, 4)
    assert result == 7
    captured = capfd.readouterr()
    assert "test_function ok" in captured.out

def test_log_error(capfd):
    with pytest.raises(TypeError):
        test_function(3, 'a')
    captured = capfd.readouterr()
    assert "test_function error:" in captured.out
