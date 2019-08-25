from typing import List
from todome.todoline import TodoLine
import pandas as pd
import re


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

    def filter(self, by=None):
        df_pos = self.df.assign(true_col=True)['true_col']  # もっといい方法ありそう
        for cond in by:
            mch_eq = re.match(r"(\S+)\=(\S+)", cond)
            mch_lt = re.match(r"(\S+)\<(\S+)", cond)
            mch_gt = re.match(r"(\S+)\>(\S+)", cond)
            mch_leq = re.match(r"(\S+)\<\=(\S+)", cond)
            mch_geq = re.match(r"(\S+)\>\=(\S+)", cond)
            mch_neq = re.match(r"(\S+)\!\=(\S+)", cond)

            # 正規表現的に，leq が引っかかるものは eq や le も引っかかるので，
            # leq/geq/neq は先に済ませちゃう
            if mch_leq is not None:
                key, cmpval = mch_leq.groups()
                df_pos = df_pos & (self.df[key].apply(str) <= cmpval)
                continue
            if mch_geq is not None:
                key, cmpval = mch_geq.groups()
                df_pos = df_pos & (self.df[key].apply(str) >= cmpval)
                continue
            if mch_neq is not None:
                key, cmpval = mch_neq.groups()
                df_pos = df_pos & (self.df[key].apply(str) != cmpval)
                continue

            if mch_eq is not None:
                key, cmpval = mch_eq.groups()
                df_pos = df_pos & (self.df[key].apply(str) == cmpval)
                continue
            if mch_lt is not None:
                key, cmpval = mch_lt.groups()
                df_pos = df_pos & (self.df[key].apply(str) < cmpval)
                continue
            if mch_gt is not None:
                key, cmpval = mch_gt.groups()
                df_pos = df_pos & (self.df[key].apply(str) > cmpval)
                continue

        return self.df[df_pos], self.df[~df_pos]

    def __str__(self):
        return "\n".join(self.df['line'])

    def to_list(self):
        return list(self.df['line'])
