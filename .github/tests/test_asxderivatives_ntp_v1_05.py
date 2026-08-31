# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class AsxderivativesNtpV105Tests(unittest.TestCase):

    def test_addordermessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_anomalousorderthresholdpublishmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/AnomalousOrderThresholdPublishMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_auctionorderexecutedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/AuctionOrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_combinationorderexecutedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/CombinationOrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_combinationsymboldirectorymessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/CombinationSymbolDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_combinationtradeexecutedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/CombinationTradeExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_equilibriumpricemessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/EquilibriumPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_futuresymboldirectorymessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/FutureSymbolDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_impliedorderaddedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/ImpliedOrderAddedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_impliedorderdeletedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/ImpliedOrderDeletedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_impliedorderreplacedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/ImpliedOrderReplacedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_openhighlowlasttradeadjustmentmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/OpenHighLowLastTradeAdjustmentMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionssymboldirectorymessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/OptionsSymbolDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookstatemessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/OrderBookStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/OrderDeletedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordervolumecancelledmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/OrderVolumeCancelledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_secondsmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/Seconds.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_textmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/TextMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradeexecutedmessage(self):
        module = "asx/asxderivatives/ntp/asxderivatives_ntp_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Asx/AsxDerivatives.Ntp.Itch.v1.05/TradeExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
