import subprocess


class Annex:
    def __init__(self):
        pass

    def test(self):
        print 'test running..'
        # setup command and direct output to a pipe.
        p1 = subprocess.Popen(
            [
                'ping',
                '-c 2',
                'google.com'
            ],
            stdout=subprocess.PIPE
        )
        output = p1.communicate()[0]
        print output

    def testAgain(self):
        host = subprocess.Popen(
            [
                'host',
                'google.com'
            ],
            stdout=subprocess.PIPE
        ).communicate()[0]
        print host
    def ls(self):
        subprocess.call(['ls', '-l'])
