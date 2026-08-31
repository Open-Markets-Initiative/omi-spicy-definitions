# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesNlsplusV40Tests(unittest.TestCase):

    def test_nlsplusregshoshortsalepricetestrestrictedindicatormessage(self):
        module = "nasdaq/nsmequities/nlsplus/nsmequities_nlsplus_v4_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v4.0/NlsPlus.RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_nlsplusstocktradingactionmessage(self):
        module = "nasdaq/nsmequities/nlsplus/nsmequities_nlsplus_v4_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v4.0/NlsPlus.StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_nlsplussystemeventmessage(self):
        module = "nasdaq/nsmequities/nlsplus/nsmequities_nlsplus_v4_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v4.0/NlsPlus.SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_nlsplustradereportlongpricemessage(self):
        module = "nasdaq/nsmequities/nlsplus/nsmequities_nlsplus_v4_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v4.0/NlsPlus.TradeReportLongPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_nlsplustradereportmessage(self):
        module = "nasdaq/nsmequities/nlsplus/nsmequities_nlsplus_v4_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v4.0/NlsPlus.TradeReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
