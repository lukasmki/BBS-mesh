import cmd


class Interface(cmd.Cmd):
    intro = "[B]ulletin [B]oard [S]ystem"
    prompt = "⌨️ Enter command ⌨️"

    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)

    def do_message(self, line):
        pass

    def do_bye(self, line):
        return True
