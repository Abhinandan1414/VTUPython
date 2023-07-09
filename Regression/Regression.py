import math
import pandas
import os
def weighted_split(original_list, weight_list,absolute_machine_speeds):
    machine_i_test_set = []
    machine_i_test_set_exec_time = []
    prev_index = 0
    for weight in weight_list:
        next_index = prev_index + math.ceil( (len(original_list) * weight) )

        machine_i_test_set.append( original_list[prev_index : next_index] )
        prev_index = next_index
    for i in range(len(weight_list)):
        machine_i_test_set_exec_time.append(sum(machine_i_test_set[i])/absolute_machine_speeds[i])
    print(machine_i_test_set)
    print(machine_i_test_set_exec_time)
    print(sum(machine_i_test_set_exec_time))

def identical_machines_total_execution_time(x,n):
    machine_i_test_set= []
    machine_i_test_set_exec_time = []
    x=sorted(x,reverse=True)
    for i in range(n):
        machine_i_test_set.append([])
    for i in range(len(x)):
        machine_i_test_set[i%n].append(x[i])
        
    for i in range(n):
        machine_i_test_set_exec_time.append(sum(machine_i_test_set[i]))
    print(machine_i_test_set)
    print(machine_i_test_set_exec_time)
    print(sum(machine_i_test_set_exec_time))

def main():
    df = pandas.read_csv(os.path.join(os.getcwd(),"Regression\\testexecutiondata.csv"),
                             sep=',')
                        
    data_set= df["execution_time"].to_list()
            
    absolute_machine_speeds = [1,2,2,1]
    weighted_machine_speeds = [.16,.32,.32,.16]
    identical_machine_speeds = [1,1,1,1]
    weighted_split(data_set,weighted_machine_speeds,absolute_machine_speeds)
    identical_machines_total_execution_time(data_set,len(identical_machine_speeds))
    
    
main()
    
    
        