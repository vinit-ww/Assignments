import re
for test_string in ['+91-9012543255', '+91-9254612315']:
    if re.match(r'^\+\d{2}-\d{10}$', test_string):
        print test_string, 'is a valid Indian local phone number'
    else:
        print test_string, 'rejected'