import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import csv
import os
import sys
import time

def generateSimilarityMatrix(src_dir):
        matrixlist = []
        with open(src_dir, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in reader:
                        matrixlist.append([float(val) for val in row])

        a = np.array(matrixlist)
        A_sparse = sparse.csr_matrix(a)
        similarities = cosine_similarity(A_sparse.transpose())

        out_dir = os.getcwd() + '/dist'

        if not os.path.exists(out_dir):
                os.makedirs(out_dir)

        np.savetxt(out_dir + "/" + src_dir.split("/")[1].split(".")[0] + "_sim_mtx.csv", similarities, delimiter=',')

def main(argv):
        arg_count = len(argv)

        if (arg_count == 2):
                src_dir = str(argv[1])

                if (src_dir == "--help" or src_dir == "-h" or src_dir == "help"):
                        print("Usage:")
                        print("python3 matrix.py <source directory>")
                else:
                        for root, dirs, files in os.walk(src_dir):
                                for idx, (file) in enumerate(files):
                                        if (file.endswith(".csv")):
                                                print("| Generating matrix from {} ({}/{})".format(str(file), str(idx + 1), str(len(files))))
                                                generateSimilarityMatrix(os.path.join(root, file))
        else:
                print("Error| argumenht required! Use help for proper usage:")
                print("python3 --help")

if __name__ == "__main__":
        start_time = time.time()
        main(sys.argv)
        end_time = time.time()

        print("\n DONE! Execution time: {}".format(str(round(end_time - start_time, 2))))