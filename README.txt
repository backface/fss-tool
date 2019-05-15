
=================================================
Admin script in progress for STWST-FSS 
=================================================

Author:(c) Michael Aschauer <m AT ash.to>
Licenced under: GPL v3
See: http://www.gnu.org/licenses/gpl.html



USAGE
======

see: 

	fss-tool.py --help


EXAMPLES:
==========


	Import files from current directory into directory "fx"
	
		fss-tool.py --import -o fx
		
	Import files from a directory
	
		fss-tool.py --import -i /home/data/ritter_archive/
		
	Import
		fss-tool.py --import -i /home/data/ritter_archive/ -o gr
		
	
	Sync wiki's page structure for directory "fx"
	
		fss-tool.py --sync-pages -i fx
