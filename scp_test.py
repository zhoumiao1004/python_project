#-*- coding:utf-8 -*-
import os
import pexpect
class Transfer(object):
	def __init__(self):
		print "Transfer Working"

	def file_transfer(self, ip, user, passwd, dst_path, filename):
		passwd_key = '.*assword.*'
		cmdline = 'scp %s %s@%s:%s' %(filename, user, ip, dst_path)
		try:
			child = pexpect.spawn(cmdline)
			child.expect(passwd_key)
			child.sendline(passwd)
			child.expect(pexpect.EOF)
			print "Transfer Work Finish!"
		except:
			print "upload failed!"

if __name__ == '__main__':
	triger = Transfer()
	exists = False
	mtime = 0
	while True:
		if (exists == False and os.path.exists('hello.txt')) \
			or (exists == True and mtime != os.path.getatime('hello.txt')):
			triger.file_transfer('192.168.150.129', 'root', 'root', '/home/luo/Desktop/', 'hello.txt')
			mtime = os.path.getatime('hello.txt')
			exists = True
			print 'file created or changed! mtime = ', mtime