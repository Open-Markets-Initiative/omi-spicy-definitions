# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CoinbasederivativesOrdersapiV18Tests(unittest.TestCase):

    def test_cancelordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/CancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderrejectmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/CancelOrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lastexecidmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/LastExecIdMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lastexecidrequestmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/LastExecIdRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loggedoutmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/LoggedOutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonconfmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/LogonConfMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/LogonMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logoutmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/LogoutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/MassCancelOrderAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/MassCancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderrejectmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/MassCancelOrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/NewOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercanceledmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/OrderCanceledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderenteredmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/OrderEnteredMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderfilledmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/OrderFilledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/OrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacedmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/OrderReplacedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pingmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/PingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pongmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/PongMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/ReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setaccountmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/SetAccountMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/SetAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_settradermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/SetTraderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_unlocktradingackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/UnlockTradingAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_unlocktradingmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.8/UnlockTradingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
