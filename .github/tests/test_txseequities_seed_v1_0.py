# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class TxseequitiesSeedV10Tests(unittest.TestCase):

    def test_definesymbolmessage(self):
        module = "txse/txseequities/seed/txseequities_seed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/DefineSymbolMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_limitorderaccepted(self):
        module = "txse/txseequities/seed/txseequities_seed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LimitOrderAccepted.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_limitordermessage(self):
        module = "txse/txseequities/seed/txseequities_seed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LimitOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonrequestmessage(self):
        module = "txse/txseequities/seed/txseequities_seed_v1_0.spicy"
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LogonRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
