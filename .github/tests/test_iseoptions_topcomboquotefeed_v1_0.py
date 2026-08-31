# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IseoptionsTopcomboquotefeedV10Tests(unittest.TestCase):

    def test_complexstrategydirectorymessage(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/ComplexStrategyDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstrategytickermessage(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/ComplexStrategyTickerMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategybestaskupdate(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyBestAskUpdate.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategybestbidandaskupdate(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyBestBidAndAskUpdate.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategybestbidupdate(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyBestBidUpdate.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyopenclosedmessage(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyOpenClosedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytradingactionmessage(self):
        module = "nasdaq/iseoptions/topcomboquotefeed/iseoptions_topcomboquotefeed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
