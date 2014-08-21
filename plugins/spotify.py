if __name__ == "__main__":
    raise Exception("This file is a plugin and cannot run independently")

import dbus

class SpotifyController:
    connected = False

    @classmethod
    def connect(cls):
        session = dbus.SessionBus.get_session()
        cls.connection = session.get_object(
            'org.mpris.MediaPlayer2.spotify',
            '/org/mpris/MediaPlayer2')
        cls.connected = True

    @classmethod
    def send_command(cls, command):
        getattr(cls.connection, command)()

    @staticmethod
    def get_controls():
        # (button text, button ID, spotify command)
        return [
            ('<', 'button_prev', 'Previous'),
            ('play/pause', 'button_playpause', 'PlayPause'),
            ('>', 'button_next', 'Next')
        ]

def get_controller():
    return SpotifyController
