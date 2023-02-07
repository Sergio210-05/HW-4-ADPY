import types


def flat_generator(list_of_list):
    concatenated_list = []

    def concatenate(list_of_list):
        for i in list_of_list:
            if not isinstance(i, list):
                concatenated_list.append(i)
            else:
                concatenate(i)
        return concatenated_list

    concatenated_list = concatenate(list_of_list)
    # print('concatenated_list:', concatenated_list)
    return (item for item in concatenated_list)


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
