# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class BlueequitiesMemoirlastsaleV13Tests(unittest.TestCase):

    def test_instrumentdirectorymessage(self):
        module = "blueoceanats/blueequities/memoirlastsale/blueequities_memoirlastsale_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/InstrumentDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitytradingstatusmessage(self):
        module = "blueoceanats/blueequities/memoirlastsale/blueequities_memoirlastsale_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/SecurityTradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereportmessage(self):
        module = "blueoceanats/blueequities/memoirlastsale/blueequities_memoirlastsale_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/TradeReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionstatusmessage(self):
        module = "blueoceanats/blueequities/memoirlastsale/blueequities_memoirlastsale_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/TradingSessionStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
