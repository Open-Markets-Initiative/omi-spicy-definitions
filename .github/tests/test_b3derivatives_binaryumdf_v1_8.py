# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class B3derivativesBinaryumdfV18Tests(unittest.TestCase):

    def test_securitydefinitionmessage(self):
        module = "b3/binaryumdf/b3derivatives_binaryumdf_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryUmdf.Sbe.v1.8/SecurityDefinitionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencemessage(self):
        module = "b3/binaryumdf/b3derivatives_binaryumdf_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryUmdf.Sbe.v1.8/Sequence.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
