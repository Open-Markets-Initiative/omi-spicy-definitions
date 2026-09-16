# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IexequitiesDeepV108Tests(unittest.TestCase):

    def test_auctioninformationmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/AuctionInformationMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_operationalhaltstatusmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/OperationalHaltStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pricelevelbuyupdatemessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/PriceLevelBuyUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pricelevelsellupdatemessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/PriceLevelSellUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retailliquidityindicatormessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/RetailLiquidityIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securityeventmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/SecurityEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsalepriceteststatusmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/ShortSalePriceTestStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereportmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/TradeReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_08.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.08/TradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
