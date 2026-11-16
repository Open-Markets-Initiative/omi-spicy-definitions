# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SpectraOrderslogincrementalV800Tests(unittest.TestCase):

    def test_bestpricesmessage(self):
        module = "moex/spectra/orderslogincremental/spectra_orderslogincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v8.0.0/BestPricesMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        module = "moex/spectra/orderslogincremental/spectra_orderslogincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v8.0.0/OrderExecutionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderupdatemessage(self):
        module = "moex/spectra/orderslogincremental/spectra_orderslogincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v8.0.0/OrderUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
