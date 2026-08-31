# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class EurexT7EobiV130Tests(unittest.TestCase):

    def test_addcomplexinstrument(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/AddComplexInstrument.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crossrequest(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/CrossRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionsummary(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/ExecutionSummary.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fullorderexecution(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/FullOrderExecution.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentstatechange(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/InstrumentStateChange.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentsummary(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/InstrumentSummary.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massinstrumentstatechange(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/MassInstrumentStateChange.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderadd(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/OrderAdd.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdelete(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/OrderDelete.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermodify(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/OrderModify.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermodifysameprio(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/OrderModifySamePrio.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_partialorderexecution(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/PartialOrderExecution.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_productstatechange(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/ProductStateChange.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_productsummary(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/ProductSummary.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoterequest(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/QuoteRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshotorder(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/SnapshotOrder.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_testradereport(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/TesTradeReport.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereport(self):
        module = "eurex/eobi/eurex_t7_eobi_v13_0.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eobi.Fbe.v13.0/TradeReport.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
