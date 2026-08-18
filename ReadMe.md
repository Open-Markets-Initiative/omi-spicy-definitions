# Omi Spicy Definitions

Omi [Spicy](https://docs.zeek.org/projects/spicy/ "A parser generator for network protocols and file formats") definitions describe common binary exchange protocols as declarative Spicy grammars, so the wire format parses with the Spicy toolchain and the Zeek network security monitor.


These definitions are built and tested with the Spicy toolchain: [spicyc](https://docs.zeek.org/projects/spicy/en/latest/toolchain.html "The Spicy parser compiler")
## Usage

Each .spicy file is a self contained module for one protocol version: a public entry unit for the transport framing and message dispatch, one unit per message, and an enum per coded field. Compile a definition to a precompiled parser (HLTO) with the Spicy compiler:

```
spicyc -j iex/iexequities/tops/iexequities_tops_v1_66.spicy -o iexequities_tops.hlto
```
The precompiled parser loads into `spicy-driver` for stand alone parsing, or into Zeek through a `.evt` interface for protocol analysis.

For compiler and toolchain information: [Spicy Toolchain](https://docs.zeek.org/projects/spicy/en/latest/toolchain.html "The Spicy toolchain")
## Development

Updates are greatly appreciated; however, this entire repository is source generated...including the words you are reading right now. If you wish to suggest definition updates, the recommended process is to create an issue with changes and explanation.  Time permitting, we will update the models and regenerate.

| Protocol Count | Generated Lines |
| --- | --- |
| 23 | 4916 |

## Testing

[![Build](https://github.com/Open-Markets-Initiative/omi-spicy-definitions/actions/workflows/build.yml/badge.svg)](https://github.com/Open-Markets-Initiative/omi-spicy-definitions/actions/workflows/build.yml)

Please report any parsing errors as an [issue](https://github.com/Open-Markets-Initiative/omi-spicy-definitions/issues "Omi Spicy Issues").  Include a small note on the protocol and version, and a minimal capture demonstrating the problem. Also consider including a link or pdf specification documenting the correct behavior.

## Open Markets Initiative

The Open Markets Initiative (Omi) is a group of technologists dedicated to enhancing the stability of electronic financial markets using modern development methods.

For a list of Omi Hft projects: [Omi Projects](https://github.com/Open-Markets-Initiative/Directory/tree/main/Projects "Open Markets Initiative Projects")

For details of Omi rules and regulations: [Omi Directory](https://github.com/Open-Markets-Initiative/Directory "Open Markets Initiative Directory")
## Organizations

> Investors Exchange · National Association of Securities Dealers Automated Quotations (Nasdaq)

## Related Definitions

The Open Markets Initiative provides protocol definitions in several formats:

- [Kaitai Struct Definitions][Kaitai.Definitions.Repository] — cross language binary parsers with the kaitai struct compiler
- [DFDL Definitions][Dfdl.Definitions.Repository] — declarative DFDL schemas for cross language parsing
- [P4 Definitions][P4.Definitions.Repository] — P4 programs for software and hardware data planes
## Disclaimer

Any similarities between existing people, places and/or protocols is purely incidental.

Enjoy.

[Kaitai.Definitions.Repository]: https://github.com/Open-Markets-Initiative/omi-kaitai-struct-definitions "Omi Kaitai Struct Definitions"
[Dfdl.Definitions.Repository]: https://github.com/Open-Markets-Initiative/omi-dfdl-definitions "Omi DFDL Definitions"
[P4.Definitions.Repository]: https://github.com/Open-Markets-Initiative/omi-p4-definitions "Omi P4 Definitions"

[Omi Projects]: https://github.com/Open-Markets-Initiative/Directory/tree/main/Projects "Open Markets Initiative Projects"
[Omi Rules and Regulations]: https://github.com/Open-Markets-Initiative/Directory/tree/main/License "Open Markets Initiative Rules and Regulations"
