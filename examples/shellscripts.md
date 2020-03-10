## Here is an example of running python and capturing output.

```python {cmd}
import subprocess

process = subprocess.run(['python', 'an_error_every_time.py'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

stdout, stderr = process.stdout, process.stderr
print("stdout\n", '-' * 20)
print(stdout.decode('utf-8'))
print("stderr\n", '-' * 20)
print(stderr.decode('utf-8'))
```

## Here is an example of running python from a string.

```python {cmd}
import subprocess

code = """
print("Hello, World")
"""

filename = 'running_chunk.py'

# Write the file.
with open(filename, 'w') as outfile:
    outfile.write(code)

process = subprocess.run(['python', filename],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)

print(process.stdout.decode())

# Delete the file.
subprocess.run(['rm', filename])
```
