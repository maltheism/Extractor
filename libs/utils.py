
class Parser:
    def __init__(self):
        pass

    def read_annex_data(self, data):
        print '(START) reading annex data:'
        print data
        # loop line by line (the data).
        for line in data.splitlines():
            print 'line is: ' + line.strip()
            print 'arr is:'
            arr = (line.strip()).split('=')
            print arr
        # # the Elitist C-style loop.
        # for i in range(0, len(data), 1):
        #     print data[i:i+1]

        print 'fin.'

