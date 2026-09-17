# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IcefuturesMdfV1133Tests(unittest.TestCase):

    def test_addormodifymessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/AddOrModifyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/DeleteOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketsnapshotmessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/MarketSnapShotMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketsnapshotordermessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/MarketSnapshotOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketstatisticsmessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/MarketStatisticsMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_messagebundlemarker(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/MessageBundleMarker.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newoptionsstrategydefinintionmessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/NewOptionsStrategyDefinintionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_specialfieldmessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/SpecialFieldMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "ice/icefutures/mdf/icefutures_mdf_v1_1_33.spicy"
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.33/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
