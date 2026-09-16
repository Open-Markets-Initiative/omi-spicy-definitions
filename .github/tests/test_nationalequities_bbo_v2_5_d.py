# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NationalequitiesBboV25DTests(unittest.TestCase):

    def test_messagesequence(self):
        module = "nyse/nationalequities/bbo/nationalequities_bbo_v2_5_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.Bbo.Pillar.v2.5.d/MessageSequence.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quotemessage(self):
        module = "nyse/nationalequities/bbo/nationalequities_bbo_v2_5_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.Bbo.Pillar.v2.5.d/QuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/nationalequities/bbo/nationalequities_bbo_v2_5_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.Bbo.Pillar.v2.5.d/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/nationalequities/bbo/nationalequities_bbo_v2_5_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.Bbo.Pillar.v2.5.d/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
