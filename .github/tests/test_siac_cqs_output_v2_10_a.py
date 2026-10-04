# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacCqsOutputV210ATests(unittest.TestCase):

    def test_endofdaymessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/EndOfDayMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_finraclosemessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/FinraCloseMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_finraopenmessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/FinraOpenMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lineintegritymessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/LineIntegrityMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_longquotemessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/LongQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketwidecircuitbreakerdeclinelevelstatusmessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/MarketWideCircuitBreakerDeclineLevelStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofdaymessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/StartOfDayMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolreferencedatamessage(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/SymbolReferenceDataMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
