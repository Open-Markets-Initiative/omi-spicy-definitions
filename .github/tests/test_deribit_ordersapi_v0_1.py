# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class DeribitOrdersapiV01Tests(unittest.TestCase):

    def test_amendorderrejectmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/AmendOrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_amendorderrequestmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/AmendOrderRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_amendorderresponsemessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/AmendOrderResponseMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderrequestmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/CancelOrderRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderresponsemessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/CancelOrderResponseMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massquoterejectmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/MassQuoteRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massquoterequestmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/MassQuoteRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massquoteresponsemessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/MassQuoteResponseMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderrejectmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/NewOrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderrequestmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/NewOrderRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderresponsemessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/NewOrderResponseMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderfilledmessage(self):
        module = "coinbase/deribit/ordersapi/deribit_ordersapi_v0_1.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/OrderFilledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
