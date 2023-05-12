import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if isinstance(loc,int) or isinstance(loc,float):
        if isinstance(scale,int) or isinstance(scale,float):
            if isinstance(lower_bound,int) or isinstance(lower_bound,float):
                if isinstance(upper_bound,int) or isinstance(upper_bound,float):
                    if lower_bound < upper_bound:
                        a = []
                        gaussian_dist = np.array(a)
                        for x in range(0,99):
                            buffer = np.random.normal(loc,scale)
                            gaussian_dist = np.append(gaussian_dist,buffer)                        
                        
                        print("Typ gaussian_dist:" + str(type(gaussian_dist)))
                        print("Typ lower_bound:" + str(type(lower_bound)))
                        print("Typ upper_bound:" + str(type(upper_bound)))
                        mask = (gaussian_dist<upper_bound) & (gaussian_dist>lower_bound)
                        mean = np.mean(gaussian_dist[mask])
                        std = np.std(gaussian_dist[mask])
                        print(type(gaussian_dist[56]))
                        print(gaussian_dist)
                        return (mean,std)
                    else:
                        raise TypeError("Lower_bound ist bigger than upper_bound!")
                else:
                    raise TypeError("upper_bound is neither int nor float")      
            else:
                raise TypeError("lower_bound is neither int nor float")
        else:
            raise TypeError("scale is neither int nor float")
    else:
        raise TypeError("loc is neither int nor float")
    

    

if __name__ == "__main__":
    # use this for your own testing!
    print(gaussian_analysis(0,1,1,10))
    
