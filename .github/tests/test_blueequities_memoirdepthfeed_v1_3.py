# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class BlueequitiesMemoirdepthfeedV13Tests(unittest.TestCase):

    def test_orderaddedmessage(self):
        module = "blueoceanats/blueequities/memoirdepthfeed/blueequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirDepthFeed.Sbe.v1.3/OrderAddedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletedmessage(self):
        module = "blueoceanats/blueequities/memoirdepthfeed/blueequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirDepthFeed.Sbe.v1.3/OrderDeletedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "blueoceanats/blueequities/memoirdepthfeed/blueequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirDepthFeed.Sbe.v1.3/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreducedmessage(self):
        module = "blueoceanats/blueequities/memoirdepthfeed/blueequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirDepthFeed.Sbe.v1.3/OrderReducedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
