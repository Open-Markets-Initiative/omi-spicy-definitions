# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class MxSolamulticastV114Tests(unittest.TestCase):

    def test_optionmarketdepthmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14/OptionMarketDepthMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optiontrademessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14/OptionTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyauctionbeginningmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14/StrategyAuctionBeginningMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyinstrumentkeymessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14/StrategyInstrumentKeyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategymarketdepthmessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14/StrategyMarketDepthMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytrademessage(self):
        module = "tmx/mx/solamulticast/mx_solamulticast_v1_14.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14/StrategyTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
