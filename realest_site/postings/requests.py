from enum import Enum


class PostingCategory(Enum):
    APARTMENT = 1
    HOUSE = 2
    ESTATE = 3
    COMMERCIAL = 4


def input_to_category(input_name: str) -> PostingCategory:
    try:
        input_number = int(input_name[-1])
    except ValueError:
        raise ValueError(
            "To convert input_name to category,"
            f" the input_name must be in the form of 'choiceN', not {input_name}"
        )
    return PostingCategory(input_number)
