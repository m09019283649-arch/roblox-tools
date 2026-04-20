from typing import Any, Dict, List, Union


def flatten_list(nested_list: List[Union[List[Any], Any]]) -> List[Any]:
    """Flatten a nested list into a single list."
    result: List[Any] = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries into one."
    merged: Dict[str, Any] = dict1.copy()
    merged.update(dict2)
    return merged


def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers."
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def string_to_dict(input_string: str) -> Dict[str, str]:
    """Convert a string of key=value pairs to a dictionary."
    return dict(item.split('=') for item in input_string.split(','))