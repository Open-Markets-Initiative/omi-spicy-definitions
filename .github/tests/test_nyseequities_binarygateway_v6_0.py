# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesBinarygatewayV60Tests(unittest.TestCase):

    def test_closeresponse(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/CloseResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_equitiessymbolreferencedatamessage(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/EquitiesSymbolReferenceDataMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportmessage(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/ExecutionReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginmessage(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/LoginMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponse(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/LoginResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordersingleandcancelreplacerequestmessage(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/NewOrderSingleAndCancelReplaceRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_open(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/Open.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_openresponse(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/OpenResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderandcancelreplaceacknowledgementmessage(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/OrderAndCancelReplaceAcknowledgementMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamavail(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v6_0_serverpillarmessage.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/StreamAvail.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
