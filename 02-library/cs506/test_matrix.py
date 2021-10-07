from cs506.matrix import get_determinant
from cs506 import read
import pytest

@pytest.mark.parametrize('test_input,expected_data',[
    (
        [[10, 20, 30], [10, 20, 30], [10, 20, 30]],0
    ),
    (
        [[10, 20, 4], [10, -20, 30], [6, 20, 9]],-4720
    ),
])
                                            

def test_matrix(test_input, expected_data):
    print(test_input)
    actual_data = get_determinant(test_input)
    assert int(actual_data) == expected_data


