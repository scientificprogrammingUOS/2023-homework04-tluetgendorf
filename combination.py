import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a,b,axis=0):
    # delete the NotImplementedError when you write your function.
    #a_rows=a.shape[0]
    #a_cols=a.shape[1]
    #a = np.reshape(a,1)

    #b_rows=b.shape[0]
    #b_cols=b.shape[1]
    print(a)
    a = np.ndarray.flatten(a)
    #a = np.append(a,6)
    #print(a.shape)
    print(a)
    print("")
    #print(b.shape)
    #print(b)
    b = np.ndarray.flatten(b)
    #b = np.append(b,1)
    #print(b.shape)
    print(b)
    print("")
    #print(a_cols)
    #print(b.shape)
    #print(b_cols)
    c = np.concatenate([a,b],axis)
    print(c)
    return c
if __name__ == "__main__":
    # use this for your own testing!
    a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    b = np.ones((2,2))
    #print(b)
    print(combination(a,b))
    
