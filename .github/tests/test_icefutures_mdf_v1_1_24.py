# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IcefuturesMdfV1124Tests(unittest.TestCase):

    def test_addormodifyordermessage(self):
        module = "ice/mdf/icefutures_mdf_v1_1_24.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/AddOrModifyOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketstatechangemessage(self):
        module = "ice/mdf/icefutures_mdf_v1_1_24.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/MarketStateChangeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newoptionsstrategydefinitionmessage(self):
        module = "ice/mdf/icefutures_mdf_v1_1_24.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/NewOptionsStrategyDefinitionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_openpricemessage(self):
        module = "ice/mdf/icefutures_mdf_v1_1_24.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/OpenPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_preopenpriceindicatormessage(self):
        module = "ice/mdf/icefutures_mdf_v1_1_24.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/PreOpenPriceIndicatorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
