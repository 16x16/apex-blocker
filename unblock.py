import os

# Get list of our blocking rules
output = os.popen('netsh advfirewall firewall show rule name=all dir=out | find "ApexBlock"').read().splitlines()
rule_list = [line.split(':')[1].strip() for line in output]

# Delete rules from the firewall
for rule in rule_list:
    os.system(f'netsh advfirewall firewall delete rule name="{rule}"')
