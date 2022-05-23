"""
This python script filters the IPs given in the input file by given latency,
saving low and high ping times to a file.
"""
from cmath import inf
from ping3 import ping
import sys
from concurrent.futures import ThreadPoolExecutor
import urllib3


def get_latency(ip):
    """
    Ping an IP address 3 times and return the average latency.
    """
    cum_latency = 0
    for i in range(3):
        try:
            result = ping(ip, unit="ms")
        except Exception:
            result = inf
        if not result:
            result = inf
        cum_latency += result
    return cum_latency / 3


if len(sys.argv) != 2:
    print("Usage: py -3 filter.py <latency threshold>")
    exit(1)

latency_threshold = float(sys.argv[1])

print("Getting latest Multiplay server list from github...")
http = urllib3.PoolManager()
r = http.request(
    'GET',
    'https://raw.githubusercontent.com/16x16/apex-blocker/master/multiplay_servers.txt'
)
with open("multiplay_servers.txt", "wb") as f:
    f.write(r.data)
print("Done!")

with open("multiplay_servers.txt") as ip_file:
    ips = ip_file.read().splitlines()

print("Pinging IPs... This could take 10+ minutes...")

# Get the average latency for each IP
with ThreadPoolExecutor(max_workers=40) as executor:
    latency_list = list(executor.map(get_latency, ips))

# Save the IPs with low latency to a file
with open("low_latency.txt", "w") as low_file:
    with open("high_latency.txt", "w") as high_file:
        for ip, latency in zip(ips, latency_list):
            if latency <= latency_threshold:
                low_file.write(f"{ip}\t{latency}\n")
            else:
                high_file.write(f"{ip}\t{latency}\n")

print('Pinging done! Saved low latency IPs to low_latency.txt and high latency IPs to high_latency.txt')
