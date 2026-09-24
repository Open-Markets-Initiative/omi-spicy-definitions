# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class PearlequitiesExpressordersV26Tests(unittest.TestCase):

    def test_cancelorderrequest(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/CancelOrderRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderresponse(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/CancelOrderResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorreducesizeordernotification(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/CancelOrReduceSizeOrderNotification.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_clientheartbeat(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/ClientHeartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequest(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/LoginRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponse(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/LoginResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordernotification(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/NewOrderNotification.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderrequest(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/NewOrderRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderpriceupdatenotification(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/OrderPriceUpdateNotification.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_serverheartbeat(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/ServerHeartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolupdate(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/SymbolUpdate.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemstatenotification(self):
        module = "miax/pearlequities/expressorders/pearlequities_expressorders_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/SystemStateNotification.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
