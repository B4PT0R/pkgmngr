"""
Script to run all tests for pypkg
"""
import pytest
import sys


if __name__ == "__main__":
    sys.exit(pytest.main(["-v"]))
