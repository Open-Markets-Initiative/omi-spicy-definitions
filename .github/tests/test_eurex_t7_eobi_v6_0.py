# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class EurexT7EobiV60Tests(unittest.TestCase):

    def test_fullorderexecution(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/FullOrderExecution.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentsummary(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/InstrumentSummary.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderadd(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/OrderAdd.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermodify(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/OrderModify.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_productsummary(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/ProductSummary.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshotorder(self):
        module = "eurex/eobi/eurex_t7_eobi_v6_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v6.0/SnapshotOrder.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
