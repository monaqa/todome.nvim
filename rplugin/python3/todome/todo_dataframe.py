from typing import List
from todome.todoline import TodoLine
import pandas as pd


class TodoDataFrame:
    def __init__(self, lines):
        if lines[-1] == '\n':
            lines = lines[:-1]
        todolines = [TodoLine(l) for l in lines.split('\n')]
        l_dict = [t.to_dict() for t in todolines]
        self.df = pd.DataFrame(l_dict)

    def sort(self, by=None, ascending=True):
        self.df.sort_values(
            by=by, ascending=ascending,
            inplace=True,
            kind='mergesort',  # choose mergesort for stability
            na_position='last',
        )

    def __str__(self):
        return "\n".join(self.df['line'])

    def to_list(self):
        return list(self.df['line'])
