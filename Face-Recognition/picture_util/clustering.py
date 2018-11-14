from sklearn.cluster import DBSCAN
import numpy as np

def cluster(encoding):
    clt = DBSCAN(eps=0.22, min_samples=2, metric="euclidean")
    X = clt.fit(encoding)
    # print(X)

    # label 결정
    label_ids = np.unique(clt.labels_)
    num_unique_faces = len(np.where(label_ids > -1)[0])
    # print("clustered %d unique faces." % num_unique_faces)
    # print(len(label_ids))
    # print("===============")

    count = 0
    final = 0
    for label_id in label_ids:
        dir_name = "ID%d" % label_id
        # print(dir_name)

        # find all indexes of label_id
        indexes = np.where(clt.labels_ == label_id)[0]
        # print(indexes)

        if label_id > -1:
                count += len(indexes)
                final += len(indexes)
        else:
                final += len(indexes)

    # print(count, final, " ", round(count / final * 100, 2), "%")
        
