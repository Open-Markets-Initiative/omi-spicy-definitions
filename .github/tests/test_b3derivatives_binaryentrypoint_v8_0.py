# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class B3derivativesBinaryentrypointV80Tests(unittest.TestCase):

    def test_establishackmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/EstablishAckMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_establishrejectmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/EstablishRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_negotiaterejectmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/NegotiateRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retransmissionmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/RetransmissionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retransmitrejectmessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/RetransmitRejectMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencemessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/SequenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_terminatemessage(self):
        module = "b3/binaryentrypoint/b3derivatives_binaryentrypoint_v8_0.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.0/TerminateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
