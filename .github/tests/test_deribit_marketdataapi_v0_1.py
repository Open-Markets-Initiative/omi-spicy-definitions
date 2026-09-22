# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class DeribitMarketdataapiV01Tests(unittest.TestCase):

    def test_askdeletemessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/AskDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_askputmessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/AskPutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_askqtyreducedmessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/AskQtyReducedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_biddeletemessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/BidDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bidputmessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/BidPutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bidqtyreducedmessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/BidQtyReducedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofcyclemessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/EndOfCycleMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentmessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/InstrumentMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshottrailermessage(self):
        module = "coinbase/deribit/marketdataapi/deribit_marketdataapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/SnapshotTrailerMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
