# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class ArcaoptionsDeepfeedV13ATests(unittest.TestCase):

    def test_outrightmarketdepthbuymessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/OutrightMarketDepthBuyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightmarketdepthsellmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/OutrightMarketDepthSellMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightseriesstatusmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/OutrightSeriesStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshoutrightmarketdepthbuymessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/RefreshOutrightMarketDepthBuyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshoutrightmarketdepthsellmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/RefreshOutrightMarketDepthSellMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_seriesindexmappingmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/SeriesIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamidmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/StreamIdMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_underlyingindexmappingmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/UnderlyingIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_underlyingstatusmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Xdp.v1.3.a/UnderlyingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
