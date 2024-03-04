import numpy as np
def main():
    array = np.array([[1,0],[5,10],[3,21],[2.6,40],[101,200]])

    def logfact(x):
        x = np.int32(x)
        val = 0 
        for i in range(1,x+1):
            val = val + np.log(i) 
        return val 

    def p(l,k):
        l = np.int32(l)
        k = np.float32(k)
        val = k*np.log(l) - l - logfact(k)
        return np.exp(val)

    result_array = []

    for element in array:
        result_array.append(p(element[0], element[1]))
    np.savetxt('part1.txt',result_array)

if __name__ == '__main__':
    main()