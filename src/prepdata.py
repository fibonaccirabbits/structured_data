#Preps dummy data
#import stuff

import os

contents = open('cor6_6.fasta').read().split('>')
for content in contents[1:]:
	parts = content.splitlines()
	outname = 'fasta6/' + parts[0].split()[0] + '.fasta'
	outcontent = '>' + '\n'.join(parts)
	outfile = open(outname ,'w')
	outfile.write(outcontent)
	outfile.close()	
