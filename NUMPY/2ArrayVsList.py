import timeit
# %timeiit - can only be used in juptyer notebook
print(timeit.timeit('[j**4 for j in range(1,9)]', number=1000000))

import numpy as np
print(timeit.timeit('np.arange(1,9)**4', setup='import numpy as np', number=1000000))