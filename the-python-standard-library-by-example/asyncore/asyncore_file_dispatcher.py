
import asyncore


class FileReader(asyncore.file_dispatcher):

    def writable(self):
        return False

    def handle_read(self):
        data = self.recv(64)
        print('READ: (%d)\n%r' % (len(data), data))

    def handle_expt(self):
        # Ignore events that look like out of band data
        pass

    def handle_close(self):
        self.close()


reader = FileReader(open('lorem.txt', 'rb'))
asyncore.loop()
