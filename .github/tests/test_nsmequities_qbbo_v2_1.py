# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesQbboV21Tests(unittest.TestCase):

    def test_bbobboquotationmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/Bbo.BboQuotationMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bboregshorestrictionmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/Bbo.RegShoRestrictionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bbostocktradingactionmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/Bbo.StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bbosystemeventmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/Bbo.SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
