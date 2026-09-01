# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class JnxequitiesPtsV16Tests(unittest.TestCase):

    def test_orderdeletedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_6.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.6/OrderDeletedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_6.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.6/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_6.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.6/OrderReplacedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsellingpricerestrictionstatemessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_6.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.6/ShortSellingPriceRestrictionStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timestampsecondsmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_6.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.6/TimestampSecondsMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
