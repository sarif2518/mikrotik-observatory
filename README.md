# MikroTik Observatory

Open-source observability platform for MikroTik networks.

Monitor your MikroTik infrastructure with real-time traffic analytics, DHCP monitoring, PPPoE tracking, and LINE alerts.

---

## Features

- 📊 Interface Traffic Monitoring
- 🌐 DHCP Client Monitoring
- 👤 PPPoE Session Tracking
- 🚨 Network Security Alerts
- 📈 Graylog Dashboard
- 🔔 LINE Messaging Alerts

---

## Architecture

MikroTik Router → Syslog → Graylog → OpenSearch → Dashboard → LINE Alerts

---

## Example Log
MTTRAFFIC if=ether1 rx_bps=390528 tx_bps=6226112
