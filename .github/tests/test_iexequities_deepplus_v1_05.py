# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IexequitiesDeepplusV105Tests(unittest.TestCase):

    def test_addordermessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_operationalhaltstatusmessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/OperationalHaltStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermodifymessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/OrderModifyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retailliquidityindicatormessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/RetailLiquidityIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securityeventmessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/SecurityEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsalepriceteststatusmessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/ShortSalePriceTestStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_05.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.05/TradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
