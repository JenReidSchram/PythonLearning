#! /usr/bin/env python

import re
import subprocess
import os

test_text = list(r'''
\\qa-vault-35.testco.com\mounted\vol20\
Total # of free bytes        : 877510377472
Total # of bytes             : 7696453464064
Total # of avail free bytes  : 877510377472

\\qa-vault-35.testco.com\mounted\vol19\
Total # of free bytes        : 832160477184
Total # of bytes             : 7696453464064
Total # of avail free bytes  : 832160477184
'''.split('\n\n'))


# Define our active volumes
# TODO: SQL query to get all active volumes in csv
active_volumes = r'\\qa-vault-35.testco.com\mounted\vol20\,\\qa-vault-35.testco.com\mounted\vol19\ '

# Convert csv values into a list (stripping out white space)
active_volumes_list = active_volumes.strip().split(',')

# Create dictionary with volumes as keys and empty string as value
storage = {}
for volume in active_volumes_list:
    storage[volume] = ''

# For each volume, run something equivalent to:
# `fsutil volume diskfree $Volume | Out-File -filepath "C:\temp\StorageList.txt" -Append`
# For now, use the test_text value

# Create regex to find Total Available Bytes
free_bytes = re.compile(r'(Total # of free bytes\s*: )(\d+)')

i = 0
for volume in storage.keys():
    if os.name == 'nt': # If this is running in Windows
        ps_str = r'fsutil volume diskfree {}'.format(volume)
        print(ps_str)
        process = subprocess.Popen(["powershell", ps_str], stdout=subprocess.PIPE)
        chunk = str(process.communicate()[0])
    else:
        chunk = test_text[i]                              # Test code: can be modified once real call is implemented

    mo = free_bytes.search(chunk)
    storage_gb = ((int(mo.group(2))/1024)/1024)/1024  # Convert byte value to GB
    storage[volume] = str(round(storage_gb, 2))
    print('Volume: {0} has available storage: {1} GB'.format(volume, storage[volume]))


# Email the report

