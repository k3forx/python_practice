import requests


class ThirdPartyMotherRequestSnackApi(object):
    def request_snack(self, child_cry):
        result = requests.get('https://snack/api', child_cry)
        return result.json()['snack']


class ChildGetSnackApi(object):
    def __init__(self, name, hungry):
        self.mother_request_api = ThirdPartyMotherRequestSnackApi()
        self.name = name
        self.hungry = hungry

    def get_snack(self):
        snack = self.mother_request_api.request_snack(
            child_cry='Iamhungry'
        )
        return snack
