# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CoinbasederivativesOrdersapiV13Tests(unittest.TestCase):

    def test_cancelordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/CancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderrejectmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/CancelOrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lastexecidmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/LastExecIdMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lastexecidrequestmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/LastExecIdRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loggedoutmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/LoggedOutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonconfmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/LogonConfMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/LogonMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logoutmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/LogoutMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/MassCancelOrderAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/MassCancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderrejectmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/MassCancelOrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/NewOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercanceledmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/OrderCanceledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderenteredmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/OrderEnteredMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderfilledmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/OrderFilledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/OrderRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacedmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/OrderReplacedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pingmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/PingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pongmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/PongMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/ReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setaccountmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/SetAccountMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/SetAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_settradermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/SetTraderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamordermessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/StreamOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_unlocktradingackmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/UnlockTradingAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_unlocktradingmessage(self):
        module = "coinbase/coinbasederivatives/ordersapi/coinbasederivatives_ordersapi_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.3/UnlockTradingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
