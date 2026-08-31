# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class MemxequitiesMemoirdepthfeedV13Tests(unittest.TestCase):

    def test_heartbeat(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderaddedmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderAddedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletedmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderDeletedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreducedmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderReducedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshowrestrictionmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/RegShowRestrictionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitytradingstatusmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/SecurityTradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/StockTradingActionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionstatusmessage(self):
        module = "memx/memxequities/memoirdepthfeed/memxequities_memoirdepthfeed_v1_3.spicy"
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/TradingSessionStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
