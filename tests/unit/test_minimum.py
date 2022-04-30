import pytest

from minimum.minimum import (
    DOES_NOT_IMPLEMENT_LESS_THAN,
    LESS_THAN_3_ELEMENTS,
    NOT_ITERABLE,
    get_minimum,
)


@pytest.mark.parametrize(
    "arr, expected_minimum",
    [
        ([4, 3, 4], 3),
        ([5, 4, 3, 4], 3),
        ([4, 3, 4, 5], 3),
        ([9, 8, 7, 6, 5, 4, 3, 4], 3),
        ([4, 3, 4, 5, 6, 7, 8, 9], 3),
        ([6, 5, 4, 3, 4, 5, 6, 7], 3),
        ([-1, -2, -3, -4, -5, -4, -3], -5),
    ],
    ids=[
        "3 elements",
        "4 elements, min to right",
        "4 elements, min to left",
        "8 elements, min to right",
        "8 elements, min to left",
        "8 elements, min at middle",
        "negative numbers",
    ],
)
def test_get_minimum(arr, expected_minimum):
    assert get_minimum(arr) == expected_minimum


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
