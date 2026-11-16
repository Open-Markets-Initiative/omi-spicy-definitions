# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class ArcaequitiesArcabookV19ATests(unittest.TestCase):

    def test_addordermessage(self):
        module = "nyse/arcaequities/arcabook/arcaequities_arcabook_v1_9_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.ArcaBook.Xdp.v1.9.a/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        module = "nyse/arcaequities/arcabook/arcaequities_arcabook_v1_9_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.ArcaBook.Xdp.v1.9.a/DeleteOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionmessage(self):
        module = "nyse/arcaequities/arcabook/arcaequities_arcabook_v1_9_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.ArcaBook.Xdp.v1.9.a/ExecutionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_imbalancemessage(self):
        module = "nyse/arcaequities/arcabook/arcaequities_arcabook_v1_9_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.ArcaBook.Xdp.v1.9.a/ImbalanceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordermessage(self):
        module = "nyse/arcaequities/arcabook/arcaequities_arcabook_v1_9_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.ArcaBook.Xdp.v1.9.a/ModifyOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
