import subprocess
import time

def perform_sweep():
    DEVICES = "/tmp/active_devices"
    file = open(DEVICES, "w")

    # Run subprocess /w call
    rp_sweep = \
        subprocess.Popen(
            ['sudo', 'arp-scan', '--interface=wlp3s0', '10.42.0.0/24'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)

    stdout, stderr = rp_sweep.communicate()
    # Avaliable Red Pitaya are a combination of registred rp and found rp
    # with arp-scan

    output = stdout.split('\n')
    for address in output:
        split = address.split('\t')
        if len(split) > 1:
            file.write("%s\n" % split[1])

    file.close()

if __name__ == "__main__":
    while 1:
        perform_sweep()
        time.sleep(1)