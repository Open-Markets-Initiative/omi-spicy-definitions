# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class B3derivativesBinaryentrypointV81Tests(unittest.TestCase):

    def test_establishmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/EstablishMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportcancelmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportmodifymessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportModifyMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportnewmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportNewMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportrejectmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreporttrademessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_negotiatemessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/NegotiateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordercrossmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/NewOrderCrossMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordersinglemessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/NewOrderSingleMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelreplacerequestmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderCancelReplaceRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelrequestmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderCancelRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermassactionreportmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderMassActionReportMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermassactionrequestmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderMassActionRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retransmitrequestmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/RetransmitRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_simplemodifyordermessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/SimpleModifyOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_simplenewordermessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_1.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/SimpleNewOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
