# MikroTik Observatory

Open-source observability platform for MikroTik networks.

Features

- MikroTik Traffic Monitoring
- DHCP client tracking
- PPPoE session monitoring
- Security alerts
- Graylog dashboard
- LINE notifications

Architecture

MikroTik -> Syslog -> Graylog -> OpenSearch -> Dashboard -> LINE

Installation

docker-compose up -d

License

MIT
