# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class LinkatsMulticastV43Tests(unittest.TestCase):

    def test_startofspinmessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/StartOfSpin.11.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofspinmessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/EndOfSpin.12.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketopenmessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/MarketOpen.13.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketclosemessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/MarketClose.14.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitymessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/Security.9.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quotemessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/Quote.1.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoteupdatemessage(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/QuoteUpdate.2.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "otcmarkets/linkats/multicast/linkats_multicast_v4_3.spicy"
        for payload in payloads.of("omi-data-packets/OtcMarkets/LinkAts.Multicast.Link.v4.3/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
