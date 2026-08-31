# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IseoptionsOrdercombofeedV11Tests(unittest.TestCase):

    def test_complexstrategyauctionmessage(self):
        module = "nasdaq/iseoptions/ordercombofeed/iseoptions_ordercombofeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/ComplexStrategyAuctionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstrategydirectorymessage(self):
        module = "nasdaq/iseoptions/ordercombofeed/iseoptions_ordercombofeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/ComplexStrategyDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstrategyorderonbookmessage(self):
        module = "nasdaq/iseoptions/ordercombofeed/iseoptions_ordercombofeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/ComplexStrategyOrderOnBookMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "nasdaq/iseoptions/ordercombofeed/iseoptions_ordercombofeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyopenclosedmessage(self):
        module = "nasdaq/iseoptions/ordercombofeed/iseoptions_ordercombofeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/StrategyOpenClosedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytradingactionmessage(self):
        module = "nasdaq/iseoptions/ordercombofeed/iseoptions_ordercombofeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/StrategyTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
