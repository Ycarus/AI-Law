import glob
import csv
import numpy as np
from sklearn.cluster import SpectralClustering
import pandas as pd
import os
import sys
import time

def generateTopic(filepath, filename):
	sim_matrix  = pd.read_csv(filepath, delimiter=",", dtype=np.dtype(float), header=None)
	mat         = np.array(sim_matrix)
	sc          = SpectralClustering(n_clusters=30, affinity='precomputed')
	topic       = sc.fit_predict(mat)
	
	output_path = '../output_spectral'
	
	if not os.path.exists(output_path):
		os.makedirs(output_path)

	np.savetxt('{}/{}_topic.txt'.format(output_path, filename), topic, '%2d', ',')


def getFilename(filepath, src_dir):
	filename = filepath.split('{}/'.format(src_dir))[1].split('.csv')[0].split('_sim_mtx')[0]

	return filename

def main(argv):
	arg_count = len(argv)

	if (arg_count == 2):
		src_dir = str(argv[1])

		if (src_dir == "--help" or src_dir == "-h" or src_dir == "help"):
			print("Usage:")
			print("python3 topic-extractor.py <source directory>")
		else:
			src_dir  = str(argv[1])
			csv_list = list(glob.iglob('{}/*.csv'.format(src_dir)))

			for idx, filepath in enumerate(csv_list):
				filename = getFilename(filepath, src_dir)
				print("| Generating topics from {} ({}/{})".format(str(filename), str(idx + 1), str(len(csv_list))))
				generateTopic(filepath, filename)
	else:
		print("Error| argumenht required! Use help for proper usage:")
		print("python3 --help")
		

if __name__ == "__main__":
        start_time = time.time()
        main(sys.argv)
        end_time = time.time()

        print("\n DONE! Execution time: {}".format(str(round(end_time - start_time, 2))))
