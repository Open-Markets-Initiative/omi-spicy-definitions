# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class TexasequitiesIntegratedfeedrefreshV25GTests(unittest.TestCase):

    def test_addorderrefreshmessage(self):
        module = "nyse/texasequities/integratedfeedrefresh/texasequities_integratedfeedrefresh_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/TexasEquities.IntegratedFeedRefresh.Pillar.v2.5.g/AddOrderRefreshMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshheadermessage(self):
        module = "nyse/texasequities/integratedfeedrefresh/texasequities_integratedfeedrefresh_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/TexasEquities.IntegratedFeedRefresh.Pillar.v2.5.g/RefreshHeaderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/texasequities/integratedfeedrefresh/texasequities_integratedfeedrefresh_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/TexasEquities.IntegratedFeedRefresh.Pillar.v2.5.g/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/texasequities/integratedfeedrefresh/texasequities_integratedfeedrefresh_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/TexasEquities.IntegratedFeedRefresh.Pillar.v2.5.g/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
