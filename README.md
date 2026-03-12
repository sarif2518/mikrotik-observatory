# MikroTik Observatory

Open-source observability platform for MikroTik networks.

![GitHub stars](https://img.shields.io/github/stars/sarif2518/mikrotik-observatory)
![GitHub forks](https://img.shields.io/github/forks/sarif2518/mikrotik-observatory)
![License](https://img.shields.io/github/license/sarif2518/mikrotik-observatory)

## Overview

MikroTik Observatory is an open-source monitoring platform designed for MikroTik routers.

It provides real-time traffic analytics, DHCP monitoring, PPPoE tracking and LINE alerts.

# Features

• Interface Traffic Monitoring  
• DHCP Client Tracking  
• PPPoE Session Monitoring  
• Network Security Alerts  
• Graylog Dashboard Integration  
• LINE Messaging Notifications  
• Lightweight Deployment with Docker  

## Architecture

MikroTik → Syslog → Graylog(Pipeline / Extractors) → OpenSearch → Dashboard → LINE Alerts

## Example Log

MTTRAFFIC if=ether1 rx_bps=390528 tx_bps=6226112

# Dashboard Preview

Example interface monitoring dashboard
![Dashboard](screenshots/dashboard.png)

## Installation
git clone https://github.com/sarif2518/mikrotik-observatory.git

## Start services
docker-compose up -d

# Project Structure
mikrotik-observatory
│
├── docker
├── mikrotik
├── parser
├── dashboards
├── alerts
├── docs
└── screenshots


---

# Roadmap

Future development plan

- MikroTik NetFlow Analyzer
- Bandwidth anomaly detection
- ISP traffic analytics
- Web UI dashboard
- Multi-router monitoring



# Contribution

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository  
2. Create a new branch  
3. Submit a pull request  




## License

MIT
