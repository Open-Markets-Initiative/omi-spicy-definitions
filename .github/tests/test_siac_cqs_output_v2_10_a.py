# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacCqsOutputV210ATests(unittest.TestCase):

    def test_a_s_symbol_reference_data(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/A_S_Symbol_Reference_Data.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_a_start_of_day(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_A_Start_of_Day.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_c_finra_close(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_C_FINRA_Close.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_o_finra_open(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_O_FINRA_Open.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_t_line_integrity(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_T_Line_Integrity.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_z_end_of_day(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_Z_End_of_Day.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_m_k_mwcb_decline_level_status(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/M_K_MWCB_Decline_Level_Status.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_q_l_long_quote(self):
        module = "siac/cqs/output/siac_cqs_output_v2_10_a.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/Q_L_Long_Quote.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
