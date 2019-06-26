import pexpect

child = pexpect.spawn('/usr/bin/ssh root@192.168.32.1')

# This line means, "wait until you see a string that matches password:"
# in the response
child.expect('password:', timeout=120) 

child.sendline('pass123') # Send the characters pass123 and "enter"

# Wait till you see a string matching prompt#
child.expect ('prompt# ')