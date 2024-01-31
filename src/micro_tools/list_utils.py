# Python program to check if two
# to get unique values from list
# using traversal
import typing

_T = typing.TypeVar('_T')


# function to get unique values
def unique(lst: typing.List[_T], comparator: typing.Callable[[typing.List[_T], _T], typing.Any] = lambda unique_list, x: x not in unique_list) -> typing.List[_T]:
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in lst:
        # check if exists in unique_list or not
        if comparator(unique_list, x):
            unique_list.append(x)
    return unique_list


def unique_by_key(lst: typing.List[_T], key_func: typing.Callable[[_T], typing.Any] = lambda x: x) -> typing.List[_T]:
    uniq_map = {}
    res = []
    for el in lst:
        key = key_func(el)
        if key not in uniq_map:
            uniq_map[key] = True
            res.append(el)

    return res


def unique_by_key_gen(lst: typing.List[_T], key_func: typing.Callable[[_T], typing.Any] = lambda x: x) -> typing.Generator[_T, None, None]:
    uniq_map = {}
    for el in lst:
        key = key_func(el)
        if key not in uniq_map:
            uniq_map[key] = True
            yield el


def group_by(lst: typing.List[_T], group_by_func: typing.Callable[[_T], typing.Any] = lambda x: x) -> typing.Dict[typing.Any, typing.List[_T]]:
    group_map = {}
    for el in lst:
        key = group_by_func(el)
        if key not in group_map:
            group_map[key] = []
        group_map[key].append(el)
    return group_map
