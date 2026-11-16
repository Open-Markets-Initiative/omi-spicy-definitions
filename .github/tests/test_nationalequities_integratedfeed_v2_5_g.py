# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NationalequitiesIntegratedfeedV25GTests(unittest.TestCase):

    def test_addordermessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crosstrademessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/CrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/DeleteOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_imbalancemessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/ImbalanceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordermessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/ModifyOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_nondisplayedtrademessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/NonDisplayedTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/OrderExecutionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/ReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/nationalequities/integratedfeed/nationalequities_integratedfeed_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeed.Pillar.v2.5.g/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
