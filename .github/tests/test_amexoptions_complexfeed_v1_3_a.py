# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class AmexoptionsComplexfeedV13ATests(unittest.TestCase):

    def test_complexcrossingrfqmessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/ComplexCrossingRfqMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexquotemessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/ComplexQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstatusmessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/ComplexStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexsymboldefinitionmessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/ComplexSymbolDefinitionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complextrademessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/ComplexTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshcomplexquotemessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/RefreshComplexQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshcomplextrademessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/RefreshComplexTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamidmessage(self):
        module = "nyse/amexoptions/complexfeed/amexoptions_complexfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.ComplexFeed.Xdp.v1.3.a/StreamIdMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
