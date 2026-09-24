# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacCtsOutputV191Tests(unittest.TestCase):

    def test_indexmessage(self):
        module = "siac/cts/output/siac_cts_output_v1_91.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v1.91/IndexMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lineintegritymessage(self):
        module = "siac/cts/output/siac_cts_output_v1_91.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v1.91/LineIntegrityMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_longtrademessage(self):
        module = "siac/cts/output/siac_cts_output_v1_91.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v1.91/LongTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shorttrademessage(self):
        module = "siac/cts/output/siac_cts_output_v1_91.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v1.91/ShortTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        module = "siac/cts/output/siac_cts_output_v1_91.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v1.91/TradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
