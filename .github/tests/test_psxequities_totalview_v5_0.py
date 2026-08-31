# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class PsxequitiesTotalviewV50Tests(unittest.TestCase):

    def test_addordernompidattributionmessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/AddOrderNoMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addorderwithmpidattributionmessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/AddOrderWithMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/OrderCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/OrderExecutedWithPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacemessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/OrderReplaceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshoshortsalepricetestrestrictedindicatormessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessagenoncross(self):
        module = "nasdaq/psxequities/totalview/psxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/PsxEquities.TotalView.Itch.v5.0.20230822/TradeMessageNon-cross.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
