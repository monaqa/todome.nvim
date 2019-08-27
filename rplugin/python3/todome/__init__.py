import pynvim
import datetime as dt

from .todoline import TodoLine
from .todo_dataframe import TodoDataFrame


@pynvim.plugin
class Main:
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim

    @pynvim.function("TodomePrettifyLines")
    def doItPython(self, args):
        self.nvim.command('echo "hello from doItPython"')

    @pynvim.command("TodomePrettify")
    def todome_prettify(self):
        buf = self.nvim.current.buffer
        l_task_lines = buf.api.get_lines(0, -1, False)
        l_tasks = [
            TodoLine(task_line).pretty_line()
            for task_line in l_task_lines]
        buf.api.set_lines(0, -1, False, l_tasks)

    @pynvim.command("TodomeSort", nargs='*', range='')
    def todome_sort(self, args, range):
        buf = self.nvim.current.buffer
        l_lines = buf.api.get_lines(0, -1, False)
        l_task_lines = Main.remove_empty_tasks(l_lines)
        tdf = TodoDataFrame('\n'.join(l_task_lines))
        tdf.sort(by=args)
        buf.api.set_lines(0, -1, False, tdf.to_list())

    @pynvim.command("TodomeFilter", nargs='*')
    def todome_filter(self, args):
        buf = self.nvim.current.buffer
        l_lines = buf.api.get_lines(0, -1, False)
        l_task_lines = Main.remove_empty_tasks(l_lines)
        tdf = TodoDataFrame('\n'.join(l_task_lines))
        df_pos, df_neg = tdf.filter(by=args)
        todo_list = [(
            "# === Matched tasks === (TodomeFilter {})"
            .format(" ".join(args))
        )]
        todo_list.extend(list(df_pos["line"]))
        todo_list.append("")
        todo_list.append("# === Unmatched tasks ===")
        todo_list.extend(list(df_neg["line"]))
        buf.api.set_lines(0, -1, False, todo_list)
        pass

    @staticmethod
    def remove_empty_tasks(l_lines: list):
        return [line for line in l_lines if not TodoLine.is_empty_task(line)]

    @pynvim.function("TodomeAddPriority")
    def add_priority(self, args):
        buf = self.nvim.current.buffer
        _, l, _, _ = self.nvim.call('getpos', '.')
        line = buf.api.get_lines(l - 1, l, False)
        td = TodoLine(line[0])
        td.priority = args[0]
        buf.api.set_lines(l - 1, l, False, [td.pretty_line()])

        # # if visual mode
        # l_lines = buf.api.get_lines(range[0], range[1], False)
        # l_after_lines = []
        # for line in l_lines:
        #     td = TodoLine(line)
        #     td.priority = priprity
        #     l_after_lines.append(td.pretty_line())
        # buf.api.set_lines(range[0], range[1], False, l_after_lines)

    @pynvim.function("TodomeToggleDone")
    def toggle_done(self, args):
        buf = self.nvim.current.buffer
        _, l, _, _ = self.nvim.call('getpos', '.')
        line = buf.api.get_lines(l - 1, l, False)
        td = TodoLine(line[0])
        if td.done:
            td.done = False
            td.done_date = None
        else:
            td.done = True
            td.done_date = dt.date.today().strftime("%Y-%m-%d")
        buf.api.set_lines(l - 1, l, False, [td.pretty_line()])
