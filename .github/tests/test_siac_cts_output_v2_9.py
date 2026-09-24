# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacCtsOutputV29Tests(unittest.TestCase):

    def test_lineintegritymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_9.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.9/LineIntegrityMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_longtrademessage(self):
        module = "siac/cts/output/siac_cts_output_v2_9.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.9/LongTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        module = "siac/cts/output/siac_cts_output_v2_9.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.9/TradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
