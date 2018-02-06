from pprint import pprint, pformat
from collections import Counter
from types import GeneratorType


__all__ = ('FrequencyTable',)

class FrequencyTable:

    def __init__(self, data, name):
        self.data = data[name]
        self.name = name

    def get_row_with_label(self, n):
        return [self.class_labels[n], *self.get_row(n)]

    def get_row(self, n: int) -> list:
        return self.frequncy_table[n]

    def get_column(self, n: int) -> GeneratorType:
        for i in self.frequncy_table:
            yield i[n]

    @property
    def frequncy_table(self) -> list:
        return [list(x.values()) for x in self.values]

    @property
    def labels(self) -> list:
        return list(self.values[0].keys())

    @property
    def values(self) -> list:
        return list(self.data.values())

    @property
    def class_labels(self) -> list:
        return list(self.data.keys())

    @property
    def number_of_rows(self) -> int:
        return len(self.frequncy_table)

    @property
    def number_of_columns(self) -> int:
        return len(self.frequncy_table[0])
    
    def __repr__(self):
        return '''
        +{}+
        |{:^32}|
        +{}+
        |{:>24}|
        +{}+
        {}
        '''.format(
            32 * '-',
            self.name,
            32 * '-',
            '{:<10}{:^20}'.format('\t','  |  '.join(self.labels)),
            32 * '-',
            [self.get_row_with_label(i) for i in range(self.number_of_rows)]
            )



