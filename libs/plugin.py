import config
import openscience


class Extractor:
    def __init__(self):
        print 'Extractor: init started.'
        # loris "username & password" required.
        self.loris = openscience.Loris(
            config.Settings.url,
            config.Settings.username,
            config.Settings.password
        )
        # online status (successful login or not) of loris.
        self.status = self.loris.login()
        print 'Extractor: init finished.'

    def refresh(self):
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # loris login was successful.
        if self.status:
            print 'Extractor is online.'
            candidates = self.loris.candidates()
            print candidates
        else:
            print 'Extractor is offline.'
