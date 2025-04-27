import cmd
from message_processing import process_message
from meshtastic.serial_interface import SerialInterface


class Interface(cmd.Cmd):
    intro = "[B]ulletin [B]oard [S]ystem"
    prompt = "> "

    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.interface = DummySerialInterface()

    def do_message(self, line):
        # process message
        process_message(self.interface.id, line, self.interface, is_sync_message=False)

    def do_bye(self, line):
        return True


class DummySerialInterface:
    bbs_nodes = []
    allowed_nodes = []

    def __init__(self, sender_id=1234567890):
        self.id: int = sender_id
        self.nodes = {sender_id: {"num": 1234567890, "user": {"shortName": "SELF"}}}

    def sendText(
        self,
        text: str,
        destinationId: int = 1234567890,
        wantAck: bool = False,
        wantResponse: bool = False,
        onResponse=None,
        channelIndex: int = 0,
        portNum: int = 0,
    ):
        print(f"SYSTEM REPONSE:\n{text}")
