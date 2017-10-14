import os
import sys
import time
import glob
from collections import OrderedDict

def getFilename(filepath, src_dir):
	filename = filepath.split('{}/'.format(src_dir))[1].split('.csv')[0].split('_sim_mtx')[0]
	return filename

def main(argv):
	arg_count = len(argv)

	if (arg_count == 3):
		src_dir           = str(argv[1])
		freq_dist_src_dir = str(argv[2])

		if (src_dir == "--help" or src_dir == "-h" or src_dir == "help"):
			print("Usage:")
			print("python3 topic-extractor.py <source directory> <frequency distibution directory>")
		else:
			src_dir  = str(argv[1])
			file_list = list(glob.iglob('{}/*.txt'.format(src_dir)))

			# for idx, filepath in enumerate(cluster_list):
			# 	print(filepath)
				# filename = getFilename(filepath, src_dir)
				# print("| Generating topics from {} ({}/{})".format(str(filename), str(idx + 1), str(len(csv_list))))
				# generateTopic(filepath, filename)


			for idx, filepath in enumerate(file_list):
				print(filepath)
				# clustered dict contains the indexes of the features names by cluster from the topic.tx file
				clustered_dict = OrderedDict()
				total_cluster_val = 0

				with open(filepath) as f:
					topic_array = f.read().splitlines()

				for cluster in range(30):
					cluster_arr = []

					for idx, t in enumerate(topic_array):
						if (cluster == int(t)):
							cluster_arr.append(idx)

					clustered_dict['cluster_{}'.format(str(cluster))] = cluster_arr
					# total_cluster_val += len(cluster_arr) 

				# print(total_cluster_val)
				# print(clustered_dict)
				
				# Access value of the collection
				# for k, v in clustered_dict.items():
				# 	print(k, v)
				filename = getFilename(filepath, src_dir)

				with open('{}/{}/full_freq_dist.csv'.format(freq_dist_src_dir, filename), 'r') as f:
					reader = csv.reader(f)
					
					for row in reader:
						print row

	else:
		print("Error| argumenht required! Use help for proper usage:")
		print("python3 --help")

if __name__ == "__main__":
        start_time = time.time()
        main(sys.argv)
        end_time = time.time()

        print("\n DONE! Execution time: {}".format(str(round(end_time - start_time, 2))))