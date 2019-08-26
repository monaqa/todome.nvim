import re


class TodoLine:
    """
    タスク1行を表すオブジェクト．
    todo.txt の仕様に概ね沿っている．

    Attributes
    ----------

    line: str
        タスク本文．
    done: bool
        タスクが完了したか否か．
    priority: str or None
        優先度．'A'-'Z' の26種類のみで，'A' から順に優先度が下がる．
    due_date: str or None
        ※ 今後型が datetime 型に変更になる可能性あり
        期限日．
    done_date: str or None
        ※ 今後型が datetime 型に変更になる可能性あり
        タスクの追加日．
    done_date: str or None
        ※ 今後型が datetime 型に変更になる可能性あり
        タスクの完了日．
    projects: list of str
        タスクが要素として持つプロジェクト．
        line 中に `+project1` と記述があれば，
        'project1' という文字列が projects 内に入ることになる．
    contexts: list of str
        タスクが要素として持つ文脈．
        line 中に `@phone` と記述があれば，
        'phone' という文字列が contexts 内に入ることになる．
    metadata: dict (key: str, value: str)
        タスク中に含まれるメタ情報．
        `key:value` の形で line 中に含まれる情報を格納する．
    text: str
        上記の属性以外に書かれているすべての情報．

    """

    def __init__(self, line: str):
        self.line = line
        self.done = TodoLine._extract_done(line)
        self.priority = TodoLine._extract_priority(line)
        self.due_date = TodoLine._extract_due_date(line)
        self.add_date = TodoLine._extract_add_date(line, self.done)
        self.done_date = TodoLine._extract_done_date(line, self.done)
        self.projects = TodoLine._extract_projects(line)
        self.contexts = TodoLine._extract_contexts(line)
        self.metadata = TodoLine._extract_metadata(line)
        self.text = TodoLine._extract_text(line)

    def pretty_line(self) -> str:
        """
        現在の attributes に格納されている情報をもとに，
        統一された形式の line を返す．
        なお，self.line 自体は変更しない．
        """
        l_text = []

        if self.done:
            l_text.append("x")
        if self.done_date is not None:
            l_text.append(self.done_date)
        if self.priority is not None:
            l_text.append("({})".format(self.priority))
        if self.add_date is not None:
            l_text.append(self.add_date)
        if self.due_date is not None:
            l_text.append("<{}>".format(self.due_date))

        l_text.append(self.text)

        l_text.extend(["+{}".format(prj) for prj in self.projects])
        l_text.extend(["@{}".format(ctx) for ctx in self.contexts])
        l_text.extend(["{}:{}".format(k, v) for k, v in self.metadata.items()])

        return " ".join(l_text)

    def to_dict(self):
        """
        属性を dict 形式に格納して返す．
        DataFrame を作成する場合に有用．
        """
        d = {}
        d['line'] = self.line
        d['done'] = self.done
        d['priority'] = self.priority
        d['due_date'] = self.due_date
        d['add_date'] = self.add_date
        d['done_date'] = self.done_date
        d['projects'] = self.projects
        d['contexts'] = self.contexts
        d['metadata'] = self.metadata
        d['text'] = self.text
        return d

    @staticmethod
    def _extract_done(line):
        """
        Extract whether the task is done or not.

        Examples
        --------
        >>> TodoLine._extract_done("x hogehoge task @example")
        True
        >>> TodoLine._extract_done("x 1978-06-25 hogehoge task @example")
        True
        >>> TodoLine._extract_done("1978-06-25 hogehoge task @example")
        False
        >>> TodoLine._extract_done("x-hogehoge task @example")
        False

        """
        mch = re.match(r"^x\s+", line)
        return (mch is not None)

    @staticmethod
    def _extract_priority(line):
        """
        Extract priority from the task.

        Examples
        --------
        >>> TodoLine._extract_priority("(A) 1978-06-25 hogehoge")
        'A'
        >>> TodoLine._extract_priority("(B) hogehoge")
        'B'
        >>> TodoLine._extract_priority("x (C) hogehoge")
        'C'
        >>> TodoLine._extract_priority("x 1988-06-25 (B) 1978-06-25 hogehoge")
        'B'
        >>> TodoLine._extract_priority("hogehoge")
        >>> TodoLine._extract_priority("(-) hogehoge")
        >>> TodoLine._extract_priority("(B)hogehoge")
        >>> TodoLine._extract_priority("(hog) ehoge")
        >>> TodoLine._extract_priority("(h) ogehoge")

        """
        mch = re.match(r"^(x\s+(\d{4}-\d{2}-\d{2}\s+)?)?\(([A-Z])\)\s+", line)
        if mch is None:
            return None
        return mch.groups()[-1]

    @staticmethod
    def _extract_add_date(line, is_done):
        """
        Extract add_date from the task.

        Examples
        --------
        >>> TodoLine._extract_add_date("(A) 1978-06-25 hogehoge", False)
        '1978-06-25'
        >>> TodoLine._extract_add_date("x (A) <2019-08-26> 優先度省略 +プロジェクトX @phone", True)
        >>> TodoLine._extract_add_date("x 2019-08-23 (A) <2019-08-26> 優先度省略 +プロジェクトX @phone", True)
        >>> TodoLine._extract_add_date("x (A) 2019-08-23 <2019-08-26> 優先度省略 +プロジェクトX @phone", True)
        '2019-08-23'

        """
        if not is_done:
            mch = re.match(r"^(\([A-Z]\)\s+)?(\d{4}-\d{2}-\d{2})\s+", line)
            if mch is None:
                return None
            return mch.groups()[1]

        # 完了済みの場合
        mch = re.match(
            r"^(x\s+(\d{4}-\d{2}-\d{2}\s+)?)?(\([A-Z]\)\s+)?((\d{4}-\d{2}-\d{2})\s+)?",
            line)
        if mch is None:
            return None
        grp = mch.groups()
        return grp[4]

    @staticmethod
    def _extract_done_date(line, is_done):
        """
        Extract done_date from the task.

        Examples
        --------
        >>> TodoLine._extract_done_date("x (A) 1978-06-25 hogehoge", True)
        """
        if not is_done:
            return None

        mch = re.match(r"^x\s+(\d{4}-\d{2}-\d{2})\s+", line)
        if mch is None:
            return None
        return mch.groups()[0]

    @staticmethod
    def _extract_projects(line):
        """
        Extract the list of projects from the task.

        Examples
        --------
        >>> TodoLine._extract_projects("(A) 1978-06-25 hogehoge +project1")
        ['project1']
        """
        l_groups = re.findall(r"(\s|^)\+(\S+)(?=\s|$)", line)
        if not l_groups:
            return []
        return [grp[1] for grp in l_groups]

    @staticmethod
    def _extract_contexts(line):
        """
        Extract the list of contexts from the task.

        Examples
        --------
        >>> TodoLine._extract_contexts("(A) 1978-06-25 hogehoge @phone")
        ['phone']
        """
        l_groups = re.findall(r"(\s|^)@(\S+)(?=\s|$)", line)
        if not l_groups:
            return []
        return [grp[1] for grp in l_groups]

    @staticmethod
    def _extract_due_date(line):
        """
        Extract done_date from the task.

        Examples
        --------
        >>> TodoLine._extract_due_date("(A) 1978-06-25 <1978-06-30> hogehoge")
        '1978-06-30'
        """
        l_groups = re.findall(r"<(\d{4}-\d{2}-\d{2})>", line)
        if not l_groups:
            return None
        return l_groups[0]

    @staticmethod
    def _extract_text(line):
        """
        Extract the main text of the task.

        Examples
        --------
        >>> TodoLine._extract_text("(A) 1978-06-25 hogehoge")
        'hogehoge'
        >>> TodoLine._extract_text("x 2019-08-23 <2019-08-26> 優先度省略 +プロジェクトX @phone")
        '優先度省略'
        """

        to_delete = [
            r"^x\s+(\d{4}-\d{2}-\d{2})\s+",
            r"^x\s+",
            r"^\(([A-Z])\)\s+",
            r"(\s|^)(\S+):(\S+)(\s|$)",
            r"<\d{4}-\d{2}-\d{2}>",
            r"\d{4}-\d{2}-\d{2}",
            r"\+\S+",
            r"@\S+",
            r"^\s*",
            r"\s*$",
        ]
        for d in to_delete:
            line = re.sub(d, "", line)
        return line

    @staticmethod
    def _extract_metadata(line):
        """
        Extract metadata (i.e., `key:value` expression) from the task.

        Examples
        --------
        >>> TodoLine._extract_metadata("(A) 1978-06-25 hogehoge tag:fuga")
        {'tag': 'fuga'}
        """
        l_groups = re.findall(r"(\s|^)(\S+):(\S+)(\s|$)", line)
        if not l_groups:
            return {}
        d = {}
        for grp in l_groups:
            d[grp[1]] = grp[2]
        return d

    @staticmethod
    def is_empty_task(line):
        """
        タスク本文を引数にとり，
        それが空のタスク（空行 or コメント行）であるかどうかを判定する．
        """
        if line == "":
            return True
        if re.match("#", line) is not None:
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
