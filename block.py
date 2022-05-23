import os
import sys


def slice_list(s, step):
    if s is not None:
        return [s[x:x+step] for x in range(0, len(s), step)]
    else:
        return []


if len(sys.argv) != 2:
    print("Usage: py -3 block.py <IPs file>")
    exit(1)

with open(sys.argv[1]) as ip_file:
    ip_list = [ip.split('\t')[0] for ip in ip_file.read().splitlines()]

for i, ip_block in enumerate(slice_list(ip_list, 500)):
    # Creating blocking rule
    os.system(f'netsh advfirewall firewall add rule name="ApexBlock{i}" dir=out action=block remoteip=111.111.111.111')

    # Creating a netsh script
    netsh_script = f"pushd advfirewall firewall set rule name=\"ApexBlock{i}\" new remoteip={','.join(ip_block)}"

    # Executing the netsh script
    with open('netsh.nsh', 'w') as netsh_file:
        netsh_file.write(netsh_script)

    os.system('netsh -f netsh.nsh')

    os.remove('netsh.nsh')
