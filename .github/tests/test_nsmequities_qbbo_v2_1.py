# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesQbboV21Tests(unittest.TestCase):

    def test_bboquotationmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/BboQuotationMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshorestrictionmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/RegShoRestrictionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/nsmequities/qbbo/nsmequities_qbbo_v2_1.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Qbbo.Itch.v2.1/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
