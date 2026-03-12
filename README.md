# MikroTik Observatory

Open-source observability platform for MikroTik networks.

![GitHub stars](https://img.shields.io/github/stars/YOURNAME/mikrotik-observatory)
![GitHub forks](https://img.shields.io/github/forks/YOURNAME/mikrotik-observatory)
![License](https://img.shields.io/github/license/YOURNAME/mikrotik-observatory)

## Overview

MikroTik Observatory is an open-source monitoring platform designed for MikroTik routers.

It provides real-time traffic analytics, DHCP monitoring, PPPoE tracking and LINE alerts.

## Features

- Interface traffic monitoring
- DHCP client tracking
- PPPoE monitoring
- Security alerts
- Graylog dashboard
- LINE notifications

## Architecture

MikroTik → Syslog → Graylog → OpenSearch → Dashboard → LINE Alerts

## Example Log

MTTRAFFIC if=ether1 rx_bps=390528 tx_bps=6226112

## Installation

git clone https://github.com/YOURNAME/mikrotik-observatory.git

## License

MIT
