#!/usr/bin/env python

DESC=""" Validate clustering of metagenomic contigs """

from argparse import ArgumentParser
import pandas as p
from itertools import combinations

def main(args):
    clustering_df  = p.read_csv(args.clustering_file, header=None, names=["contig", "cluster"], index_col=0)
    correct_df = p.read_csv(args.correct_file, header=None, names=["contig", "cluster"], index_col=0)
    clustering_df['correct'] = correct_df['cluster']
    
    for correct_name, cluster in clustering_df.groupby("correct"):
        for 
    print recall(clustering_df, correct_df)


def recall(clustering_df, correct_df):
    # Estimated number of clusters
    number_of_clusters = len(clustering_df.cluster.unique())
    number_of_contigs = len(clustering_df)


    avg_TP = 0
    for i, cluster in correct_df.groupby(['cluster']):
        TP = 0
        contigs_in_cluster = len(cluster)
        for c1, c2 in combinations(cluster.index, 2):
            if clustering_df.ix[c1] == clustering_df.ix[c2]:
                TP += 1
        avg_TP += TP/float(contigs_in_cluster)
    return avg_TP/float(number_of_clusters)
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('clustering_file', 
                        help=("Clustering file output, e.g. clustering.csv "
                              "from CONCOCT. File should be in csv format "
                              "where the first column is contig id and the "
                              "second is the cluster name that the contig "
                              "has been assigned to."))
    parser.add_argument('correct_file',
                        help=("Correct clustering file, in the same format "
                              "as the clustering_file"))
    parser.add_argument('--ofile', default="Conf.csv", 
                        help=("Output file for confusion matrix, default "
                              "is 'Conf.csv'"))

    args = parser.parse_args()
    main(args)
