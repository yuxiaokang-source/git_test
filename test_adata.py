import scanpy as sc 
print(sc.__version__)
import numpy as np
a=np.array([[1,2,3],[2,33,1],[1,2,1],[0,0,0]])

adata=sc.AnnData(a)
bb=adata[[0,0,1],[2,2,1]]
print(adata)
print(bb)

## 这里可以看到就是说 scanpy1.4.2是无法进行同时slice的，但是scanpy1.7.2是可以的。