# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesIntegratedfeedV23ATests(unittest.TestCase):

    def test_addorderrefreshmessage(self):
        module = "nyse/nyseequities/integratedfeed/nyseequities_integratedfeed_v2_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.IntegratedFeed.Xdp.v2.3.a/AddOrderRefreshMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_refreshheadermessage(self):
        module = "nyse/nyseequities/integratedfeed/nyseequities_integratedfeed_v2_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.IntegratedFeed.Xdp.v2.3.a/RefreshHeaderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/nyseequities/integratedfeed/nyseequities_integratedfeed_v2_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.IntegratedFeed.Xdp.v2.3.a/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/nyseequities/integratedfeed/nyseequities_integratedfeed_v2_3_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.IntegratedFeed.Xdp.v2.3.a/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
