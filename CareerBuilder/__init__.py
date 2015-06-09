import requests
import xmltodict


class CareerBuilder:
    _base_api_url = 'http://api.careerbuilder.com'

    @property
    def base_api_url(self):
        return "%s/%s/" % (self._base_api_url, self.api_version)

    def __init__(self,
                 developer_key,
                 api_version="v2",
                 base_url=None):
        self.developer_key = developer_key
        self.api_version = api_version
        if base_url:
            self._base_api_url = base_url

    def _api_call(self, url, **kwargs):
        response = {
                'url': self.base_api_url + url,
        }
        payload = {
            'DeveloperKey': self.developer_key,
        }
        payload = dict(payload.items() + kwargs.items())
        resp = requests.get(response['url'], params=payload)
        response['xml'] = resp.text
        response['result'] = xmltodict.parse(response['xml'])
        response['payload'] = payload
        return response

    def application(self, job_id, **kwargs):
        kwargs['JobDID'] = job_id
        return self._api_call('appliation/blank', **kwargs)

    def categories(self, **kwargs):
        return self._api_call('categories', **kwargs)

    def education_codes(self, **kwargs):
        return self._api_call('educationscodes', **kwargs)

    def employee_types(self, **kwargs):
        return self._api_call('employeetypes', **kwargs)

    def job(self, job_id, **kwargs):
        kwargs['DID'] = job_id
        return self._api_call('job', **kwargs)

    def job_search(self, **kwargs):
        return self._api_call('jobsearch', **kwargs)

    def recommendations(self, job_id, **kwargs):
        kwargs['JobDID'] = job_id
        return self._api_call('recommendations/forjob', **kwargs)
