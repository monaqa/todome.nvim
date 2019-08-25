import re


class TodoLine:
    def __init__(self, line: str):
        self.line = line
        self.done = self._extract_done(line)
        self.priority = self._extract_priority(line)
        self.due_date = self._extract_due_date(line)
        self.add_date = self._extract_add_date(line)
        self.done_date = self._extract_done_date(line)
        self.projects = self._extract_projects(line)
        self.contexts = self._extract_contexts(line)
        self.metadata = self._extract_metadata(line)
        self.text = self._extract_text(line)

    def pretty_line(self) -> str:
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

    def _extract_done(self, line):
        mch = re.match(r"^x\s+", line)
        return (mch is not None)

    def _extract_priority(self, line):
        mch = re.match(r"^(x\s+(\d{4}-\d{2}-\d{2})?)?\(([A-Z])\)", line)
        if mch is None:
            return None
        return mch.groups()[-1]

    def _extract_add_date(self, line):
        if not self.done:
            mch = re.match(r"^(\([A-Z]\)\s+)?(\d{4}-\d{2}-\d{2})\s+", line)
            if mch is None:
                return None
            return mch.groups()[1]

        # 完了済みの場合
        mch = re.match(
            r"^(x\s+(\d{4}-\d{2}-\d{2}\s+)?)?(\([A-Z]\)\s+)?(\d{4}-\d{2}-\d{2})?\s+",
            line)
        if mch is None:
            return None
        grp = mch.groups()
        return grp[3]

    def _extract_done_date(self, line):
        if not self.done:
            return None

        mch = re.match(r"^x\s+(\d{4}-\d{2}-\d{2})\s+", line)
        if mch is None:
            return None
        return mch.groups()[0]

    def _extract_projects(self, line):
        l_groups = re.findall(r"(\s|^)\+(\S+)(?=\s|$)", line)
        if not l_groups:
            return []
        return [grp[1] for grp in l_groups]

    def _extract_contexts(self, line):
        l_groups = re.findall(r"(\s|^)@(\S+)(?=\s|$)", line)
        if not l_groups:
            return []
        return [grp[1] for grp in l_groups]

    def _extract_due_date(self, line):
        l_groups = re.findall(r"<(\d{4}-\d{2}-\d{2})>", line)
        if not l_groups:
            return None
        return l_groups[0]

    def _extract_text(self, line):
        to_delete = [
            r"^(x\s+(\d{4}-\d{2}-\d{2})?)?\(([A-Z])\)",
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

    def _extract_metadata(self, line):
        l_groups = re.findall(r"(\s|^)(\S+):(\S+)(\s|$)", line)
        if not l_groups:
            return {}
        d = {}
        for grp in l_groups:
            d[grp[1]] = grp[2]
        return d

