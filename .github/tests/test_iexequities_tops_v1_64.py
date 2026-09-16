# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IexequitiesTopsV164Tests(unittest.TestCase):

    def test_auctioninformationmessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/AuctionInformationMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_officialpricemessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/OfficialPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_operationalhaltstatusmessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/OperationalHaltStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoteupdatemessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/QuoteUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitydirectorymessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/SecurityDirectoryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsalepriceteststatusmessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/ShortSalePriceTestStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereportmessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/TradeReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_64.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/TradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
