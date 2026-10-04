# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacCtsOutputV211BTests(unittest.TestCase):

    def test_consolidatedstartofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/ConsolidatedStartOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofdaymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/EndOfDayMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofendofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/EndOfEndOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofstartofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/EndOfStartOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionalapproximateadjustedvolumemarketcentermessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalApproximateAdjustedVolumeMarketCenterMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionalconsolidatedendofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalConsolidatedEndOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionallongtrademessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalLongTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionalparticipantendofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalParticipantEndOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionalpriordaytradecancelerrormessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalPriorDayTradeCancelErrorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionalpriordaytrademessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalPriorDayTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fractionaltradecancelerrormessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/FractionalTradeCancelErrorMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lineintegritymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/LineIntegrityMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketwidecircuitbreakerdeclinelevelstatusmessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/MarketWideCircuitBreakerDeclineLevelStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_participantstartofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/ParticipantStartOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofdaymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/StartOfDayMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofendofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/StartOfEndOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofstartofdaysummarymessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/StartOfStartOfDaySummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolreferencedatamessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/SymbolReferenceDataMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        module = "siac/cts/output/siac_cts_output_v2_11_b.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/TradingStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
