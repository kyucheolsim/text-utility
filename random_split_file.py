import argparse
import random

PARAM = None
parser = argparse.ArgumentParser()
parser.add_argument(
	'-i', '--input_file', type=str,
	default='', help=''
	)
parser.add_argument(
	'-p', '--prefix', type=str,
	default='split_file_', help=''
	)
parser.add_argument(
	'-r', '--ratio', type=float,
	default=0.5, help=''
	)
parser.add_argument(
	'--skip-head' ,action='store_true',
	default=False, help=''
	)
PARAM = parser.parse_args()

with open(PARAM.input_file, 'r') as fin:
	if PARAM.skip_head:
		data = fin.readlines()[1:]
	else:
		data = fin.readlines()

	random.shuffle(data)
	total = len(data)
	cut = int(total * PARAM.ratio)
	print("total: {}, sp1: {}, sp2: {}".format(total, cut, total - cut))

with open(PARAM.prefix + '1.txt', 'w') as fout:
	fout.writelines(data[:cut])

with open(PARAM.prefix + '2.txt', 'w') as fout:
	fout.writelines(data[cut:])
