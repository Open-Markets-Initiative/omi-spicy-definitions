# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class EurexT7XtiV100Tests(unittest.TestCase):

    def test_orderexecresponse(self):
        module = "eurex/xti/eurex_t7_xti_v10_0_server.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Xti.Fbe.v10.0/OrderExecResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
