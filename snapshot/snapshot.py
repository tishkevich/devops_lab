#!/usr/bin/env python

import psutil
import argparse
from datetime import datetime
import time
import json


class Snapshot:
    """Create a snapshot of the state of the system every 5 minutes"""

    def __init__(self, interval=300, out_format="txt"):
        self.interval = interval
        self.out_format = out_format

    def get_state(self):
        timestamp = datetime.now().isoformat()
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        io_read = psutil.disk_io_counters().read_bytes
        io_write = psutil.disk_io_counters().write_bytes
        net_packets_sent = psutil.net_io_counters().packets_sent
        net_packets_recv = psutil.net_io_counters().packets_recv
        return timestamp, cpu, memory, io_read, io_write, net_packets_sent, net_packets_recv

    def write_file(self, snapshot_number=1, filename="snapshot.txt"):
        data = self.get_state()
        out_string = "SNAPSHOT " + str(snapshot_number) + ": " + str(data[0]) + ": "\
                     + ", ".join(map(str, data[1:])) + "\n"
        with open(filename, 'a') as out:
            out.write(out_string)

    def write_json(self, snapshot_number=1, filename="snapshot.json"):
        raw_data = self.get_state()
        columns = ("Timestamp", "CPU_load", "Memory_load", "IO_read_bytes", "IO_write bytes",
                   "net_packets_sent", "net_packets_recv")
        data = {"SNAPSHOT " + str(snapshot_number): dict(zip(columns, raw_data))}
        with open(filename, 'a') as out:
            json.dump(data, out, indent=2)

    def run(self):
        i = 1
        while True:
            if self.out_format == "txt":
                self.write_file(i)
            elif self.out_format == "json":
                self.write_json(i)
            time.sleep(self.interval)
            i += 1


def main():
    parser = argparse.ArgumentParser("Take snapshot of the system's state")
    parser.add_argument("--interval", help="snapshot interval, sec (default: 5 m)",
                        default=300, type=int)
    parser.add_argument("--out", help="output file format (txt or json, default: txt)",
                        default="txt", type=str)
    args = parser.parse_args()
    snapshot = Snapshot(args.interval, args.out)
    snapshot.run()


if __name__ == "__main__":
    main()
