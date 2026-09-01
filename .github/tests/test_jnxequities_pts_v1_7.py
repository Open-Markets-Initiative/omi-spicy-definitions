# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class JnxequitiesPtsV17Tests(unittest.TestCase):

    def test_orderaddedwithoutattributesmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/OrderAddedWithoutAttributesMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/OrderDeletedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/OrderReplacedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_secondsmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/SecondsMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsellingpricerestrictionstatemessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/ShortSellingPriceRestrictionStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatemessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_7_moldudp64.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Itch.v1.7/TradingStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
