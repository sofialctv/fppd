# -*- coding: utf-8 -*-
"""Fundamentos PP_D_04.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iovOldF-dAzx81t4A6SPERDla3C3Yhpe

**Aula 4**

Após nossa terceira  aula, onde discutimos os fundamentos da programação paralela, vamos  avaliar duas alternativas  paralelismo
"""

#importando bibliotecas necessárias
import time
import random as rd
import numpy as np
# SuperFastPython.com
# example of extending the Process class

from multiprocessing import Process

"""Atividade1

Através do problema de achar o maior e o menor de um vetor de inteiros.

Vamos comparar multi-threads e multi-processos
"""

vetor=np.random.randint(0, 1000, 100)

Múltiplas  Threads.
def do_something(sec):
  print('Doing Something...')
  time.sleep(sec)
  print('Done!')

threads=[]
start=time.time()

for _ in range(1000):
   new_thread = Thread(target=do_something, args=[1])
   threads.append(new_thread)
   new_thread.start()

for t in threads:
  t.join()



end=time.time()

print( f'Tempo decorrido:{end-start}')

#  Multi-processosa custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)

# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task, args=(1.5, 'New message from another process'))
    # run the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()

"""Referência para memória compartilhadada:

https://docs.python.org/3/library/multiprocessing.shared_memory.html
"""