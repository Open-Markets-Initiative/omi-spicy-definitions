# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NasdaqUqdfOutputV15Tests(unittest.TestCase):

    def test_limituplimitdownpricebandmessage(self):
        module = "nasdaq/uqdf/output/nasdaq_uqdf_output_v1_5.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/Uqdf.Output.Utp.v1.5/LimitUpLimitDownPriceBandMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quotelongformmessage(self):
        module = "nasdaq/uqdf/output/nasdaq_uqdf_output_v1_5.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/Uqdf.Output.Utp.v1.5/QuoteLongFormMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoteshortformmessage(self):
        module = "nasdaq/uqdf/output/nasdaq_uqdf_output_v1_5.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/Uqdf.Output.Utp.v1.5/QuoteShortFormMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
