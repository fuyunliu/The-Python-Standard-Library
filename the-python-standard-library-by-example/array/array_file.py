
import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1:', a)

# Write the array of numbers to a temporary file
with tempfile.NamedTemporaryFile() as output:
    a.tofile(output.file)  # must pass an *actual* file
    output.flush()
    print(output.name)

    output.seek(0)
    raw_data = output.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # Read the data into an array
    output.seek(0)
    a2 = array.array('i')
    a2.fromfile(output, len(a))
    print('A2:', a2)
