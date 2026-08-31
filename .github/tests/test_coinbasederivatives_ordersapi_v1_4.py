# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CoinbasederivativesOrdersapiV14Tests(unittest.TestCase):

    def test_instrumentinfomessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/InstrumentInfoMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentinforequestmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/InstrumentInfoRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loggedoutmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LoggedOutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonconfmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LogonConfMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LogonMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/MassCancelOrderAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/MassCancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/NewOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderfilledmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderFilledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacedmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderReplacedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/ReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setaccountmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/SetAccountMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/SetAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_settradermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_4.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/SetTraderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
