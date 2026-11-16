# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class AmexoptionsTopfeedV13ATests(unittest.TestCase):

    def test_outrightboldrfqmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/OutrightBoldRfqMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightcrossingrfqmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/OutrightCrossingRfqMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightquotemessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/OutrightQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightseriesstatusmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/OutrightSeriesStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrighttrademessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/OutrightTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshoutrightquotemessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/RefreshOutrightQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshoutrighttrademessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/RefreshOutrightTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamidmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Xdp.v1.3.a/StreamIdMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
