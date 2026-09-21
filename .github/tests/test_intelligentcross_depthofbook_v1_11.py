# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IntelligentcrossDepthofbookV111Tests(unittest.TestCase):

    def test_orderexecutedmessage(self):
        module = "imperative/depthofbook/intelligentcross_depthofbook_v1_11.spicy"
        for payload in payloads.of("omi-data-packets/Imperative/IntelligentCross.DepthOfBook.Aspen.v1.11/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "imperative/depthofbook/intelligentcross_depthofbook_v1_11.spicy"
        for payload in payloads.of("omi-data-packets/Imperative/IntelligentCross.DepthOfBook.Aspen.v1.11/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
