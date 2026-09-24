# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacCqsOutputV191Tests(unittest.TestCase):

    def test_longquotemessage(self):
        module = "siac/cqs/output/siac_cqs_output_v1_91.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v1.91/LongQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
