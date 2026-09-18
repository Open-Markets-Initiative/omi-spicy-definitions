# Generated transport payload extraction for pcap captures

import dpkt


def of(path):
    result = []

    with open(path, "rb") as capture:
        # a capture may be classic pcap or pcapng, which its first four bytes tell apart
        magic = capture.read(4)
        capture.seek(0)
        reader = dpkt.pcapng.Reader(capture) if magic == b"\x0a\x0d\x0d\x0a" else dpkt.pcap.Reader(capture)

        for _, frame in reader:
            packet = dpkt.ethernet.Ethernet(frame)

            if not isinstance(packet.data, dpkt.ip.IP):
                continue

            transport = packet.data.data

            if not isinstance(transport, (dpkt.udp.UDP, dpkt.tcp.TCP)):
                continue

            payload = bytes(transport.data)

            if payload:
                result.append(payload)

    return result
