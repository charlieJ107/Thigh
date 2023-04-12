##############################
# BACK-END STUFF
##############################

import sys
from pathlib import Path
import importlib

# break test if time taken for a test is more than 3-seconds
import signal  # for timing, signal library is required


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    ''' custom signal handler '''
    raise TimeoutException

# change the behaviour of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)


# Importing functions
def importModule(module_name):
    # get a handle on the module
    mdl = importlib.import_module(module_name)

    # is there an __all__?  if so respect it
    if "__all__" in mdl.__dict__:
        names = mdl.__dict__["__all__"]
    else:
        # otherwise we import all names that don't begin with _
        names = [x for x in mdl.__dict__ if not x.startswith("_")]

    # now drag them in
    globals().update({k: getattr(mdl, k) for k in names})

try:
    mod = sys.argv[1].split('.')[0]
    importModule(mod)
except IndexError as ie:
    sys.exit('Please, provide the name of the file to test.')


# Testing function
def runTest(call, output):
    if type(call) != type(output):
        return False

    if isinstance(call,list):
        if len(call) != len(output):
            return False
        for ind in range(len(call)):
            res = runTest(call[ind],output[ind])
            if not res:
                return False
    elif call != output:
        return False

    return True

##############################
# TESTCASES
##############################

# Lists of tests for each function
# Each element of the list is a (input,solution) tuple
# - 'input' is a tuple containing the input parameters.
# - 'solution' must be provided in format expected.
exercise1_list = [((1.5,0.7,2,2.3),'setosa'),
                ((1.9,1.5,2.7,2.5),'versicolor'),
                ((3,2,3.1,1.75),'virginica'),
                ((2,2,5.3,1.6),'versicolor')]

exercise2_list = [(('Maltese',9.5,6.7,True),True),
				 (('Bulldog',16,44,False),False),
				 (('Dalmatian',18,49,False),True),
				 (('Dalmatian',26,63,True),True)]

exercise3_list = [(([1,2,3,4,5],),[(1,3,3,5),(1,11,9,25)]),
				 (([7,2,4,5],),[(2,4.5,4.5,7),(4,23.5,20.5,49)]),
				  (([5,3,1,4,2],),[(1,3,3,5),(1,11,9,25)]),
				  (([2,4,5,7],),[(2,4.5,4.5,7),(4,23.5,20.5,49)])]

exercise4_list = [(({"a/0": "a/1","a/1": "a/0"},'a',['0','0','1','1','0','0']),['1','1','0','0','1','1']),
				 (({"a/0": "a/1","a/1": "b/0","b/0": "b/0","b/1": "a/1"},'a',['0','0','1','1','0','0']),['1','1','0','1','1','1']),
				 (({"0/0": "0/None","0/1": "0/None","0/\n": "0/0","1/0": "0/None","1/1": "1/None","1/\n": "1/1"},'1',['1','1','\n']),['None','None','1']),
				 (({"0/0": "0/None","0/1": "0/None","0/\n": "0/0","1/0": "0/None","1/1": "1/None","1/\n": "1/1"},'1',['1','0','1','\n']),['None','None','None','0'])]

exercise5_list = [(('test_data/text1.txt',),(128, 8, 10, 36, 3, 3)),
				  (('test_data/text2.txt',),(84, 0, 3, 19, 1, 4)),
				  (('test_data/text3.txt',),(81, 3, 12, 20, 2, 1)),
				 (('test_data/text4.txt',),(310, 0, 15, 74, 5, 3)),]

exercise6_list = [(([1,2,3],),1),
				  (([1,[2,[]],[4,5]],),3),
				  (([],),1),
				  (([1,[1,'a'],'a'],),2)]

exercise7_list = [((3,2),True),
				  ((5,2),False),
				  ((0.3,3),True),
				  ((1.15,2),False)]

exercise8_list = [(('sehuoh',),1),
				  (('caarto',),5),
				  (('abcde',),0),
				  (('abcdef',),2)]

green_1 = {1:'i',3:'c'}
yellow_1 = {'e':{3}}
gray_1 = {'r','a','s','d','f'}
green_2 = {2:'a'}
yellow_2 = {'a':{3},'i':{2},'l':{3,4},'r':{1}}
gray_2={'e','t','u','o','p','g','h','c','m','s'}
green_3 = {}
yellow_3 = {'r':{1},'i':{2},'l':{3}}
gray_3 = {'g','o','u','p','c','h'}
green_4 = {4:'r'}
yellow_4 = {'r':{1},'i':{1,2},'l':{0,3}}
gray_4 = {'g','o','u','p','c','h','t','e'}
exercise9_list = [((green_1,yellow_1,gray_1),5),
				  ((green_2,yellow_2,gray_2),3),
				  ((green_3,yellow_3,gray_3),38),
				  ((green_4,yellow_4,gray_4),1)]
exercise10_list = [((green_1,yellow_1,gray_1), {'wince', 'yince', 'mince'}),
				  ((green_2,yellow_2,gray_2),{'laari', 'liard'}),
				  ((green_3,yellow_3,gray_3),{'liter'}),
				  ((green_4,yellow_4,gray_4),{'flair'})]

##############################
# FRONT-END STUFF
##############################

# Dictionary of functions to test
test_dict = {exercise1: exercise1_list,
			 exercise2: exercise2_list,
			 exercise3: exercise3_list,
			 exercise4: exercise4_list,
			 exercise5: exercise5_list,
			 exercise6: exercise6_list,
			 exercise7: exercise7_list,
			 exercise8: exercise8_list,
			 exercise9: exercise9_list,
			 exercise10: exercise10_list}

res_list = []
# Loop on every function to test
for fun,test_list in test_dict.items():
    res = 0


    # Loop on every test to run
    for t in test_list:
        test_time_limit = 3 # per test time limit (seconds)
        param = t[0]
        sol = t[1]
        signal.alarm(test_time_limit)
        try:
            out = fun(*param)
            if not runTest(out,sol):
                err_str = 'ERROR IN {0}{1}: *** EXPECTED: {2} *** OBTAINED: {3}\n\n'.format(fun.__name__,param,sol,out)
                sys.stdout.write(err_str)
                sys.stdout.flush()
            else:
                res += 1
        except Exception as e:
            if type(e) == TimeoutException:
                e = f"TimeoutException >{test_time_limit} seconds"
            err_str = 'ERROR IN {0}{1}: '.format(fun.__name__,param) + \
                        str(e) + '\n\n'
            sys.stdout.write(err_str)
            sys.stdout.flush()
        # END for t in test_list:


    res_list.append(res)
    err_str = '#### FUNCTION {0} SCORE: {1} / {2}\n\n'.format(fun.__name__,res,len(test_list))
    sys.stdout.write(err_str)
    sys.stdout.flush()
    # END for fun_name,test_list in test_dict.items():

# print res_list as a CSV
out_str = f'{sys.argv[1]}, {", ".join(str(x) for x in res_list)}\n'
sys.stderr.write(out_str)
sys.stderr.flush()
