import pytest
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger.info('Started')

logger.debug("You need __init__.py file in each folder to support the module chaining")

from pytest_demo.src.calculator import add

# Test the method in other library
def test_calculator():
    assert add(3, 7) == 10

#############################################################3

# Write a function to raise System Error
def raise_system_error():
    raise SystemExit(1)

# Test System Error
def test_raise_system_error():
    with pytest.raises(SystemExit):
        raise_system_error()

#############################################################3

# Write a function to raise RuntimeError
def raise_run_time_error():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError(),
        ],
    )

# Test RunTimeError
def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise_run_time_error()
    assert excinfo.group_contains(RuntimeError)
    assert not excinfo.group_contains(TypeError)

