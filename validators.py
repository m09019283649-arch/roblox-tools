from typing import Any, Dict, Union

def validate_integer(value: Any, min_value: int = 0, max_value: int = 100) -> bool:
    """
    Validate if the input is an integer within a specified range.

    Args:
        value (Any): The value to validate.
        min_value (int): The minimum valid value (inclusive).
        max_value (int): The maximum valid value (inclusive).

    Returns:
        bool: True if valid, False otherwise.
    """
    if isinstance(value, int) and min_value <= value <= max_value:
        return True
    return False


def validate_string(value: Any, allowed_values: Union[None, set] = None) -> bool:
    """
    Validate if the input is a string and optionally check against allowed values.

    Args:
        value (Any): The value to validate.
        allowed_values (set, optional): A set of allowed string values.

    Returns:
        bool: True if valid, False otherwise.
    """
    if isinstance(value, str):
        if allowed_values is None or value in allowed_values:
            return True
    return False


def validate_dict_keys(data: Dict[str, Any], required_keys: set) -> bool:
    """
    Validate if all required keys are present in the dictionary.

    Args:
        data (Dict[str, Any]): The dictionary to validate.
        required_keys (set): A set of required keys.

    Returns:
        bool: True if all required keys are present, False otherwise.
    """
    return required_keys.issubset(data.keys())
