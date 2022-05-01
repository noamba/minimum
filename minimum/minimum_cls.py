from minimum.constants import (
    LESS_THAN_3_ELEMENTS,
    NOT_ITERABLE,
    DOES_NOT_IMPLEMENT_LESS_THAN,
)


class Minimum:
    def __init__(self, array):
        self.array = array
        self._validate()

    def get_minimum(self, first_index=None, last_index=None):
        """Recursive method returning the minimal element of self.array between
        the two indexes: first_index and last_index.

        Args:
            first_index: First index to check, defaults to None
            last_index: Last index to check, defaults to None

        Returns: Minimal element in the section
        """
        if first_index is None:
            first_index = 0

        if last_index is None:
            last_index = len(self.array) - 1

        section_length = last_index - first_index + 1

        # only 3 elements in the range? Return middle element - that's the minimum!
        if section_length == 3:
            return self.array[first_index + 1]

        # more than 3 elements? Reduce section size
        first_index, last_index = self._get_smaller_section(
            first_index, last_index, section_length
        )

        return self.get_minimum(first_index, last_index)

    def _validate(self):
        """Validate self.array"""
        # is iterable?
        try:
            iter(self.array)
        except TypeError:
            raise ValueError(f"{type(self.array)} {NOT_ITERABLE}")

        # at least 3 elements long?
        if len(self.array) <= 2:
            raise ValueError(LESS_THAN_3_ELEMENTS)

        # implements less than?
        try:
            self.array[0] < self.array[1]
        except TypeError:
            raise ValueError(f"{type(self.array[0])} {DOES_NOT_IMPLEMENT_LESS_THAN}")

    def _get_smaller_section(self, first_index, last_index, section_length):
        """Return first and last indexes defining a smaller section of self.array
        between first_index and last_index (the current section) where the
        minimal element must be.
        This method uses the 3 elements at the middle of the current section"""
        elements_to_mid_section = section_length // 2
        check_from_index = last_index - elements_to_mid_section - 1
        is_first_less_than_second, is_second_less_than_third = self._get_relations(
            first_element=self.array[check_from_index],
            second_element=self.array[check_from_index + 1],
            third_element=self.array[check_from_index + 2],
        )

        if is_first_less_than_second and is_second_less_than_third:  # above minimum
            return first_index, check_from_index + 1
        elif (
            not is_first_less_than_second and not is_second_less_than_third
        ):  # below minimum
            return check_from_index + 1, last_index
        else:  # spot on minimum!
            return check_from_index, check_from_index + 2

    @staticmethod
    def _get_relations(first_element, second_element, third_element):
        """Return relations between:
        * first_element and second_element and
        * second_element and third_element
        """
        return first_element < second_element, second_element < third_element
