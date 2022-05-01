import pytest

from minimum import get_minimum
from minimum.constants import (
    LESS_THAN_3_ELEMENTS,
    NOT_ITERABLE,
    DOES_NOT_IMPLEMENT_LESS_THAN,
)


@pytest.mark.parametrize(
    "array, expected_minimum",
    [
        ([4, 3, 4], 3),
        ([5, 4, 3, 4], 3),
        ([4, 3, 4, 5], 3),
        (["g", "f", "e", "d", "c", "d"], "c"),
        ([9, 8, 7, 6, 5, 4, 3, 4], 3),
        ([4, 3, 4, 5, 6, 7, 8, 9], 3),
        ([6, 5, 4, 3, 4, 5, 6, 7], 3),
        ([-1, -2, -3, -4, -5, -4, -3], -5),
    ],
    ids=[
        "3 elements",
        "4 elements, min to right",
        "4 elements, min to left",
        "non-number elements",
        "8 elements, min to right",
        "8 elements, min to left",
        "8 elements, min at middle",
        "negative numbers",
    ],
)
def test_get_minimum(array, expected_minimum):
    assert get_minimum(array) == expected_minimum


class TestValidation:
    def test_raises_not_iterable(self):
        with pytest.raises(ValueError, match=NOT_ITERABLE):
            get_minimum(3)

    def test_raises_less_than_3_elements(self):
        with pytest.raises(ValueError, match=LESS_THAN_3_ELEMENTS):
            get_minimum([3, 4])

    def test_raises_does_not_implement_less_than(self):
        class A:
            def __init__(self):
                pass

        with pytest.raises(ValueError, match=DOES_NOT_IMPLEMENT_LESS_THAN):
            get_minimum([A(), A(), A()])
