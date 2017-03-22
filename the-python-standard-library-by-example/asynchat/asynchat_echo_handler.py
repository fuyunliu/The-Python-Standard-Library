
import asynchat
import logging


class EchoHandler(asynchat.async_chat):
    """Handles echoing messages from a single client.
    """

    # Artificially reduce buffer sizes to illustrate
    # sending and receiving partial messages.
    ac_in_buffer_size = 128
    ac_out_buffer_size = 128

    def __init__(self, sock):
        self.received_data = []
        self.logger = logging.getLogger('EchoHandler')
        asynchat.async_chat.__init__(self, sock)
        # Start looking for the ECHO command
        self.process_data = self._process_command
        self.set_terminator(b'\n')

    def collect_incoming_data(self, data):
        """Read an incoming message from the client
        and put it into the outgoing queue.
        """
        self.logger.debug(
            'collect_incoming_data() -> (%d bytes) %r',
            len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        """The end of a command or message has been seen."""
        self.logger.debug('found_terminator()')
        self.process_data()

    def _process_command(self):
        """Have the full ECHO command"""
        command = b''.join(self.received_data)
        self.logger.debug('_process_command() %r', command)
        command_verb, command_arg = command.strip().split(b' ')
        expected_data_len = int(command_arg)
        self.set_terminator(expected_data_len)
        self.process_data = self._process_message
        self.received_data = []

    def _process_message(self):
        """Have read the entire message."""
        to_echo = b''.join(self.received_data)
        self.logger.debug('_process_message() echoing %r',
                          to_echo)
        self.push(to_echo)
        # Disconnect after sending the entire response
        # since we only want to do one thing at a time
        self.close_when_done()
