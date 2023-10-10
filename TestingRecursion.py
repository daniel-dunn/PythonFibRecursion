import time
import matplotlib.pyplot as plot

fib_dictionary = {
        0: 1,
        1: 1
    }

def basicFib(index):
    if(index < 2):
        return 1
    else:
        return basicFib(index - 1) + basicFib(index - 2)


def listFibA(index):
    
    if index in fib_dictionary.keys():
        return fib_dictionary.get(index)
    else:
        fib_dictionary[index] = listFibA(index-2) + listFibA(index -1)
        return listFibA(index)

def listFibB(index):
    
    if index in fib_dictionary.keys():
        return fib_dictionary.get(index)
    else:
        fib_dictionary[index] = listFibB(index-2) + listFibB(index -1)
        return listFibB(index)


def main():

    basicExecutionTime = []
    listAExecutionTime = []
    listBExecutionTime = []
    sequence = []
    
    for i in range(45) :

        sequence.append(i)
        start_time = time.time()
        basicFib(i)
        basicExecutionTime.append(time.time()-start_time)

        start_time = time.time()
        listFibA(i)
        listAExecutionTime.append(time.time()-start_time)

        



    
    plot.plot(sequence,basicExecutionTime, label = "Basic Execution Time")
    plot.plot(sequence,listAExecutionTime, label = "List (A) Execution Time")
    #plot.plot(sequence,listBExecutionTime, label = "List (B) Execution Time")

    plot.xlabel("Sequence Index")
    plot.ylabel("Time (s)")
    plot.title("Fibonacci Algorithm Process Times")
    plot.legend()
    plot.show()

    

if __name__ == "__main__":
         main()