# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class AmexoptionsDeepfeedV13ATests(unittest.TestCase):

    def test_outrightmarketdepthbuymessage(self):
        module = "nyse/amexoptions/deepfeed/amexoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.DeepFeed.Xdp.v1.3.a/OutrightMarketDepthBuyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightmarketdepthsellmessage(self):
        module = "nyse/amexoptions/deepfeed/amexoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.DeepFeed.Xdp.v1.3.a/OutrightMarketDepthSellMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshoutrightmarketdepthbuymessage(self):
        module = "nyse/amexoptions/deepfeed/amexoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.DeepFeed.Xdp.v1.3.a/RefreshOutrightMarketDepthBuyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshoutrightmarketdepthsellmessage(self):
        module = "nyse/amexoptions/deepfeed/amexoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.DeepFeed.Xdp.v1.3.a/RefreshOutrightMarketDepthSellMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamidmessage(self):
        module = "nyse/amexoptions/deepfeed/amexoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.DeepFeed.Xdp.v1.3.a/StreamIdMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
