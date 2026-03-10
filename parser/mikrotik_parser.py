import re
import json
from datetime import datetime
from typing import Optional, Dict, Any, List


class MikroTikLogParser:
    def __init__(self) -> None:
        self.traffic_pattern = re.compile(
            r"""
            ^<(?P<priority>\d+)>
            (?P<month>\w+)\s+
            (?P<day>\d+)\s+
            (?P<time>\d{2}:\d{2}:\d{2})\s+
            (?P<host>\S+)\s+
            (?P<tag>MTTRAFFIC)\s+
            if=(?P<iface>[^\s]+)\s+
            rx_bps=(?P<rx_bps>\d+)\s+
            tx_bps=(?P<tx_bps>\d+)
            """,
            re.VERBOSE,
        )

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        line = line.strip()
        if not line:
            return None

        match = self.traffic_pattern.match(line)
        if not match:
            return None

        data = match.groupdict()

        month_str = data["month"]
        day = int(data["day"])
        time_str = data["time"]
        current_year = datetime.now().year

        try:
            parsed_dt = datetime.strptime(
                f"{current_year} {month_str} {day} {time_str}",
                "%Y %b %d %H:%M:%S"
            )
        except ValueError:
            parsed_dt = None

        result = {
            "raw": line,
            "priority": int(data["priority"]),
            "host": data["host"],
            "tag": data["tag"],
            "iface": data["iface"],
            "rx_bps": int(data["rx_bps"]),
            "tx_bps": int(data["tx_bps"]),
            "rx_mbps": round(int(data["rx_bps"]) / 1_000_000, 3),
            "tx_mbps": round(int(data["tx_bps"]) / 1_000_000, 3),
            "timestamp": parsed_dt.isoformat() if parsed_dt else None,
        }

        return result

    def parse_file(self, filepath: str) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                parsed = self.parse_line(line)
                if parsed:
                    results.append(parsed)

        return results


def main() -> None:
    parser = MikroTikLogParser()

    sample_lines = [
        "<190>Mar 1 21:04:08 Gateway MTTRAFFIC if=ether1 rx_bps=390528 tx_bps=6226112",
        "<190>Mar 1 21:19:58 Gateway MTTRAFFIC if=pppoe-out1 rx_bps=58033872 tx_bps=1719344",
        "<190>Mar 1 21:20:05 Gateway MTTRAFFIC if=bridge rx_bps=1024000 tx_bps=2048000",
    ]

    for line in sample_lines:
        parsed = parser.parse_line(line)
        print(json.dumps(parsed, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
