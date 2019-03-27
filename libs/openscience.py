import json
import requests


class Loris:
    def __init__(self, url, username, password):
        print '- Loris: init started.'
        # Version number of API.
        self.version = 'v0.0.3-dev'
        # URL for accessing the API.
        self.url = url + '/api/' + self.version
        # API commands.
        self.api = {
            'login': '/login',
            'candidates': '/candidates/',
            'candidate_instruments': '/candidates/$CandID/$VisitLabel/instruments'
        }
        # Username and Password for login.
        self.username = username
        self.password = password
        # Token when successful login completes.
        self.token = ''
        # Error message details.
        self.error = ''
        print '- Loris: init finished.'

    def login(self):
        print '- Loris: login fired!'
        # login parameters for post.
        login_params = {
            'username': self.username,
            'password': self.password
        }
        # sending post request and saving the response.
        login_request = requests.post(
            url=self.url + self.api['login'],
            json=login_params,
            verify=False
        )
        try:
            # raise an exception for non-200 status code.
            login_request.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print '- Loris: login finished and failed. HTTPError!'
            self.error = str(error)
            return False
        # extracting data in json format.
        login_data = login_request.json()
        # save token if success, return true and otherwise return false.
        if 'error' in login_data:
            self.error = 'Login token contains error.'
            print '- Loris: login finished and failed.'
            return False
        else:
            self.token = login_data['token']
            print '- Loris: login finished and success.'
            return True

    def candidates(self):
        print '- Loris: candidates fired!'
        candidates_response = json.loads(requests.get(
            url=self.url + self.api['candidates'],
            verify=False,
            headers={
                'Authorization': 'Bearer %s' % self.token
            }
        ).content.decode('ascii'))
        if 'Candidates' in candidates_response:
            return candidates_response['Candidates']
        else:
            return []
