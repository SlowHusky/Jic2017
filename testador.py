# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import numbapro
import random
import time
from numpy import array

@numbapro.jit
def jited(a,b):
	return a**b
	
@numbapro.vectorize(['float64(float64, float64)'], target='parallel')
def jitedP(a,b):
	return a**b
	
def nonJited(a,b):
	return a**b
	
@numbapro.vectorize(['float64(float64, float64)'], target='gpu')
def jiteGPU(a,b):
	return a**b

if __name__=='__main__':
	print('runing test!')
	print('teste de velocidade de jit: 500 exponenciações de 2^(8e6)')
	for i in range(5):
		t1=-time.clock()
		for i in range(500):
			jited(2,8000000+i)
		t1+=time.clock()
		
		t2=-time.clock()
		for i in range(500):
			nonJited(2,8000000+i)
		t2+=time.clock()
		
		t3=-time.clock()
		for i in range(500):
			jitedP(2,8000000+i)
		t3+=time.clock()
		
		t4=-time.clock()
		for i in range(500):
			jiteGPU(2,8000000+i)
		t4+=time.clock()
		
		print('jit == %f nonjit == %f jitVecParalel == %f jitVecGPU == %f'%(t1, t2, t3, t4))
