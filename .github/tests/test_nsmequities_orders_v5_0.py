# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesOrdersV50Tests(unittest.TestCase):

    def test_canceledmessage(self):
        module = "nasdaq/nsmequities/orders/nsmequities_orders_v5_0_client.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/CanceledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelordermessage(self):
        module = "nasdaq/nsmequities/orders/nsmequities_orders_v5_0_client.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/CancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_clientheartbeatpacket(self):
        module = "nasdaq/nsmequities/orders/nsmequities_orders_v5_0_client.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/ClientHeartbeatPacket.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_enterordermessage(self):
        module = "nasdaq/nsmequities/orders/nsmequities_orders_v5_0_client.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/EnterOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderacceptedmessage(self):
        module = "nasdaq/nsmequities/orders/nsmequities_orders_v5_0_client.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/OrderAcceptedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_serverheartbeatpacket(self):
        module = "nasdaq/nsmequities/orders/nsmequities_orders_v5_0_client.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/ServerHeartbeatPacket.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
