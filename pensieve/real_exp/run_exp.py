import sys
import os
import subprocess
import numpy as np
import time

RUN_SCRIPT = 'run_video.py'
RANDOM_SEED = 43
RUN_TIME = 5  # sec
ABR_ALGO = ['fastMPC', 'robustMPC', 'RL']
#ABR_ALGO = ['BOLA']
REPEAT_TIME = 1


def main():

	np.random.seed(RANDOM_SEED)

	with open('./chrome_retry_log', 'wb') as log:
		log.write('chrome retry log\n')
		log.flush()

		for rt in xrange(REPEAT_TIME):
			#np.random.shuffle(ABR_ALGO)
			for abr_algo in ABR_ALGO:

				while True:
                    #print time.time()
					#print('HERE')
					script = 'python ' + RUN_SCRIPT + ' ' + \
								abr_algo + ' ' + str(RUN_TIME) + ' ' + str(rt)
					
					#print('HERE1')
					proc = subprocess.Popen(script,
								stdout=subprocess.PIPE, 
								stderr=subprocess.PIPE, 
								shell=True)


					#print('HERE2')	
					(out, err) = proc.communicate()
                    #print time.time()
					
					#print('HERE3')
					if out == 'done\n':
						break
					else:
						log.write(abr_algo + '_' + str(rt) + '\n')
						log.write(out + '\n')
						log.flush()



if __name__ == '__main__':
    #print time.time()
	main()
    #print time.time()
