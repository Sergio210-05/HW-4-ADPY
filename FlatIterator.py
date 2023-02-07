class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        # print("FlatIterator was created")

    def __iter__(self):
        # print('Enter in cycle')
        self.counter = 0
        concatenated_list = []

        def __concatenate(self, list_of_list):
            for i in list_of_list:
                if not isinstance(i, list):
                    concatenated_list.append(i)
                else:
                    __concatenate(self, i)
            return concatenated_list
        self.concatenated_list = __concatenate(self, self.list_of_list)
        # print('concatenated_list', self.concatenated_list)
        return self

    def __next__(self):
        if self.counter >= len(self.concatenated_list):
            raise StopIteration
        item = self.concatenated_list[self.counter]
        self.counter += 1
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
