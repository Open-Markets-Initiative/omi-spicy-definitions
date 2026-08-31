# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class AmexequitiesIntegratedfeedV21GTests(unittest.TestCase):

    def test_addordermessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_imbalancemessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/ImbalanceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/OrderExecutionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/ReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequenceresetmessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/SequenceResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/amexequities/integratedfeed/amexequities_integratedfeed_v2_1_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.IntegratedFeed.Xdp.v2.1.g/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
