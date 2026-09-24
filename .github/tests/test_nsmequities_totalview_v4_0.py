# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesTotalviewV40Tests(unittest.TestCase):

    def test_addordermessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addorderwithmpidmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/AddOrderWithMpidMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_brokentrademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/BrokenTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crosstrademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/CrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketparticipantpositionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/MarketParticipantPositionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_netorderimbalanceindicatormessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/NetOrderImbalanceIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/OrderCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/OrderExecutedWithPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stockdirectorymessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/StockDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timestampmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/TimestampMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v4_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v4.0/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
