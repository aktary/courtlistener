from django.test import TestCase
from alert.lib.string_utils import trunc


class TestStringUtils(TestCase):

    def test_trunc(self):
        """Does trunc give us the results we expect?"""
        s = 'Henry wants apple.'
        tests = (
            # Simple case
            {'length': 13, 'result': 'Henry wants'},
            # Off by one cases
            {'length': 4, 'result': 'Henr'},
            {'length': 5, 'result': 'Henry'},
            {'length': 6, 'result': 'Henry'},
            # Do we include the length of the ellipsis when measuring?
            {'length': 12, 'ellipsis': '...', 'result': 'Henry...'},
            # What happens when an alternate ellipsis is used instead?
            {'length': 15, 'ellipsis': '....', 'result': 'Henry wants....'},
            # Do we cut properly when no spaces are found?
            {'length': 2, 'result': 'He'},
            # Do we cut properly when ellipsizing if no spaces found?
            {'length': 6, 'ellipsis': '...', 'result': 'Hen...'},
            # Do we return the whole s when length >= s?
            {'length': 50, 'result': s}
        )
        for test_dict in tests:
            result = trunc(
                s=s,
                length=test_dict['length'],
                ellipsis=test_dict.get('ellipsis', None),
            )
            self.assertEqual(
                result,
                test_dict['result'],
                msg='Failed with dict: %s.\n'
                    '%s != %s' % (test_dict, result, test_dict['result'])
            )
            self.assertTrue(
                len(result) <= test_dict['length'],
                msg="Failed with dict: %s.\n"
                    "%s is longer than %s" %
                    (test_dict, result, test_dict['length'])
            )
