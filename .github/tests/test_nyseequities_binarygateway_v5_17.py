# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesBinarygatewayV517Tests(unittest.TestCase):

    def test_newordersingleandcancelreplacerequestmessage(self):
        module = "nyse/nyseequities/binarygateway/nyseequities_binarygateway_v5_17.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v5.17/NewOrderSingleAndCancelReplaceRequestMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
