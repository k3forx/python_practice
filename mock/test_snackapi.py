import unittest
from unittest.mock import MagicMock
import snackapi


class TestThirdPartyMotherRequestSnackApi(unittest.TestCase):
    def test_request_snack(self):
        result = snackapi.ChildGetSnackApi(name='hirotaka', hungry='nothungry')
        result.mother_request_api.request_snack =\
            MagicMock(return_value='senbei')

        self.assertEqual(result.get_snack(), 'senbei')
