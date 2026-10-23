# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class MxSolamulticastV1141Tests(unittest.TestCase):

    def test_optionmarketdepthmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14_1.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/OptionMarketDepthMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optiontrademessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14_1.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/OptionTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyauctionbeginningmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14_1.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyAuctionBeginningMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyinstrumentkeysmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14_1.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyInstrumentKeysMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategymarketdepthmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14_1.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyMarketDepthMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytrademessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14_1.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
