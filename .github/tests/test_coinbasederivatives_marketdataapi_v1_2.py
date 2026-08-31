# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CoinbasederivativesMarketdataapiV12Tests(unittest.TestCase):

    def test_orderdeletemessage(self):
        module = "coinbase/coinbasederivatives/marketdataapi/coinbasederivatives_marketdataapi_v1_2.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderputmessage(self):
        module = "coinbase/coinbasederivatives/marketdataapi/coinbasederivatives_marketdataapi_v1_2.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/OrderPutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordersnapshotmessage(self):
        module = "coinbase/coinbasederivatives/marketdataapi/coinbasederivatives_marketdataapi_v1_2.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/OrderSnapshotMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofoutrightinstrumentsnapshotmessage(self):
        module = "coinbase/coinbasederivatives/marketdataapi/coinbasederivatives_marketdataapi_v1_2.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/StartOfOutrightInstrumentSnapshotMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofspreadinstrumentsnapshotmessage(self):
        module = "coinbase/coinbasederivatives/marketdataapi/coinbasederivatives_marketdataapi_v1_2.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/StartOfSpreadInstrumentSnapshotMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
