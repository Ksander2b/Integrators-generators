class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.cursor = -1
        self.list_nested = []
        self.list_iter_main = iter(self.list)
        return self

    def __next__(self):
        self.cursor +=1
        if len(self.list_nested) == self.cursor:
            self.list_nested = 0
            self.cursor = 0
            while not self.list_nested:
                self.list_nested = next(self.list_iter_main)
        return self.list_nested[self.cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
