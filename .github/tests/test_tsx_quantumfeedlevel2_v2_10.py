# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class TsxQuantumfeedlevel2V210Tests(unittest.TestCase):

    def test_assigncopordersmessage(self):
        module = "tmx/tsx/quantumfeedlevel2/tsx_quantumfeedlevel2_v2_10.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Tsx.QuantumFeedLevel2.Xmt.v2.10/AssignCopOrdersMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookedmessage(self):
        module = "tmx/tsx/quantumfeedlevel2/tsx_quantumfeedlevel2_v2_10.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Tsx.QuantumFeedLevel2.Xmt.v2.10/OrderBookedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelledmessage(self):
        module = "tmx/tsx/quantumfeedlevel2/tsx_quantumfeedlevel2_v2_10.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Tsx.QuantumFeedLevel2.Xmt.v2.10/OrderCancelledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereportmessage(self):
        module = "tmx/tsx/quantumfeedlevel2/tsx_quantumfeedlevel2_v2_10.spicy"
        for payload in payloads.of("omi-data-packets/Tmx/Tsx.QuantumFeedLevel2.Xmt.v2.10/TradeReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
