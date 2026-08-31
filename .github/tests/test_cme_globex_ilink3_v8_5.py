# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CmeGlobexIlink3V85Tests(unittest.TestCase):

    def test_executionreportstatus(self):
        module = "cme/ilink3/cme_globex_ilink3_v8_5_server.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.iLink3.Sbe.v8.5/ExecutionReportStatus.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quotecancel(self):
        module = "cme/ilink3/cme_globex_ilink3_v8_5_server.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.iLink3.Sbe.v8.5/QuoteCancel.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quotecancelack(self):
        module = "cme/ilink3/cme_globex_ilink3_v8_5_server.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.iLink3.Sbe.v8.5/QuoteCancelAck.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequence(self):
        module = "cme/ilink3/cme_globex_ilink3_v8_5_server.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.iLink3.Sbe.v8.5/Sequence.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
