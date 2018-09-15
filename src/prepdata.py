#Preps dummy data
#import stuff

import os
import sys
import random

#contents = open('cor6_6.fasta').read().split('>')
#for content in contents[1:]:
#	parts = content.splitlines()
#	outname = 'fasta6/' + parts[0].split()[0] + '.fasta'
#	outcontent = '>' + '\n'.join(parts)
#	outfile = open(outname ,'w')
#	outfile.write(outcontent)
#	outfile.close()
#
for root, dirs, files in os.walk('fasta6'):
	for file in files:
		filepath = os.path.join(root, file)
		contents = open(filepath).read().splitlines()
		contents[1] = contents[1] + contents[1][random.randint(0, len(contents[1])):]
		newcontent = '\n'.join(contents[:2])
		print(newcontent)
		outfile = open(filepath, 'w')
		outfile.write(newcontent)
		outfile.close()
