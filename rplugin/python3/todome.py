import pynvim
from pynvim import Nvim


@pynvim.plugin
class Main:
    def __init__(self, nvim: Nvim):
        self.nvim = nvim

    @pynvim.function("DoItPython")
    def doItPython(self, args):
        self.nvim.command('echo "hello from doItPython"')
        self.nvim.error("hogehoge")


if __name__ == "__main__":
    import os

    nvim = pynvim.attach('socket', path=os.environ['NVIM_LISTEN_ADDRESS'])
    m = Main(nvim)
    m.doItPython([])
