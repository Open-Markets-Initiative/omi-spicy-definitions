# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NtxequitiesTotalviewV50Tests(unittest.TestCase):

    def test_addordermpidattributionmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/AddOrderMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addordernompidattributionmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/AddOrderNoMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_noncrosstrademessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/NonCrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/OrderCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/OrderExecutedWithPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacemessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/OrderReplaceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshoshortsalepricetestrestrictedindicatormessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retailinterestmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/RetailInterestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0.20230822/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
