# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesBboV25BTests(unittest.TestCase):

    def test_quotemessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_5_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Pillar.v2.5.b/QuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshheadermessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_5_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Pillar.v2.5.b/RefreshHeaderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_5_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Pillar.v2.5.b/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_5_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Pillar.v2.5.b/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
