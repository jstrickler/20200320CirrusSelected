#!/usr/bin/env python
from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob
import logging

logging.basicConfig(
    filename="subprocess.log",
    level=logging.DEBUG,
)

logging.info("Starting program")

raw_cmd = "netstat -an"
logging.debug(f"raw_cmd: {raw_cmd}")

cmd_list = shlex.split(raw_cmd)
logging.debug(f"cmd_list: {cmd_list}")

# run(cmd_list)
# run(raw_cmd, shell=True)
print('-' * 60)
try:
    proc = run(cmd_list, stdout=PIPE)
except CalledProcessError as err:
    logging.error(err)
else:
    output = proc.stdout.decode()
    for line in output.splitlines():
        if "ESTABLISHED" in line:
            print(line)

logging.info("Ending program")
