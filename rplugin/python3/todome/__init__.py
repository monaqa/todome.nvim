import pynvim

from todome.todoline import TodoLine
from todome.todo_dataframe import TodoDataFrame


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
        l_task_lines = buf.api.get_lines(0, -1, False)
        tdf = TodoDataFrame('\n'.join(l_task_lines))
        tdf.sort(by=args)
        buf.api.set_lines(0, -1, False, tdf.to_list())
