# Graylog Pipeline Notes

This document describes how MikroTik traffic logs should be parsed in Graylog.

## Example Raw Log

MTTRAFFIC if=ether1 rx=390528 tx=6226112

## Target Fields

- mt_if
- mt_rx
- mt_tx

## Example Regex

```regex
MTTRAFFIC if=(?<iface>\S+) rx=(?<rx>\d+) tx=(?<tx>\d+)
