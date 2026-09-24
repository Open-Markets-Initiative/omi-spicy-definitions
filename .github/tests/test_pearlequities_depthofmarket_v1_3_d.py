# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class PearlequitiesDepthofmarketV13DTests(unittest.TestCase):

    def test_addordermessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/DeleteOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordermessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/ModifyOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/OrderExecutionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitytradingstatusnotificationmessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/SecurityTradingStatusNotificationMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemtimemessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/SystemTimeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "miax/pearlequities/depthofmarket/pearlequities_depthofmarket_v1_3_d_udp.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.DepthOfMarket.Mach.v1.3.d/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
