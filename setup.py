from distutils.core import setup

setup(	name="fss-tools",
		version="0.1",
		author="Michael Aschauer",
		author_email="m@ash.to",
		#py_modules=['fss'],
		license='LICENSE.txt',
		description='Tools for STWST FSS / Foto Sammel Server',
		long_description=open('README.txt').read(),
		url='https://github.com/backface/fss',
		#data_files=[
		#('bin', 
		#	['exp2png.py',
		#	'exp2exp.py',
		#	'exp2svg.py',
		#	'stitchconv.py']
		#)]
		scripts=['fss-tool'],
     )
