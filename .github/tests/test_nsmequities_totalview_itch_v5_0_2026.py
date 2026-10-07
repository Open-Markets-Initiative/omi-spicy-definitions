# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesTotalviewItchV502026Tests(unittest.TestCase):

    def test_addordernompidattributionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/AddOrderNoMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addorderwithmpidattributionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/AddOrderWithMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crosstrademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/CrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_luldauctioncollarmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/LuldAuctionCollarMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketparticipantpositionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/MarketParticipantPositionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_netorderimbalanceindicatormessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/NetOrderImbalanceIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_noncrosstrademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/NonCrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderExecutedWithPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderReplaceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshoshortsalepricetestrestrictedindicatormessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stockdirectorymessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/StockDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_itch_v5_0_2026_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
