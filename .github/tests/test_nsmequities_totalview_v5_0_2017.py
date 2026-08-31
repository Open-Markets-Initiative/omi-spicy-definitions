# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesTotalviewV502017Tests(unittest.TestCase):

    def test_addordernompidattributionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/AddOrderNoMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addorderwithmpidattributionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/AddOrderWithMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crosstrademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/CrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_luldauctioncollarmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/LuldAuctionCollarMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketparticipantpositionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/MarketParticipantPositionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_multiplepackets(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/Multiple.Packets.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mwcbdeclinelevelmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/MwcbDeclineLevelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_netorderimbalanceindicatormessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/NetOrderImbalanceIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_noncrosstrademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/NonCrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/OrderCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/OrderExecutedWithPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/OrderReplaceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshoshortsalepricetestrestrictedindicatormessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stockdirectorymessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/StockDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v5_0_2017.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2017/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
