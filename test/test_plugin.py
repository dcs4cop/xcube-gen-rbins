import unittest

from xcube_gen_rbins.iproc import init_plugin


class RbinsPluginTest(unittest.TestCase):

    # noinspection PyMethodMayBeStatic
    def test_init_plugin(self):
        # Smoke test
        init_plugin()
