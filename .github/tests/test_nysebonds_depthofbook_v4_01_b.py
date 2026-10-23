# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NysebondsDepthofbookV401BTests(unittest.TestCase):

    def test_addordermessage(self):
        module = "nyse/nysebonds/depthofbook/nysebonds_depthofbook_v4_01_b_server.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseBonds.DepthOfBook.Abp.v4.01.b/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        module = "nyse/nysebonds/depthofbook/nysebonds_depthofbook_v4_01_b_server.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseBonds.DepthOfBook.Abp.v4.01.b/DeleteOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
