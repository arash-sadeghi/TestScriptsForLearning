''' Learing asyncio '''
import asyncio
import time
#! await keyword can only be used insude async wrapper
async def main():
  print('[+] sih')
  #! func('garah bujur olmiyeyde') # wont run at all
  #! await func('garah bujur olmiyeyde') # will be sequential
  task = asyncio.create_task(func('[+] garah bujur olmiyeyde')) # will be threadintg
  returned = await task # will wait the execution of tasks and return value of function will be stored in returned variable 
  #! task is like a future (promise in JS). it will be valued after await finishes
  print(f"[+] tasks returned : {returned}")
  await asyncio.sleep(0.5) # this will simply wait for 0.5 s. its awating for execution of sleep.
  print('[+] girde')

  #! testing gather:
  funcs = [func1 , func2]
  await asyncio.gather(*[i in funcs]) #! star is for unpacking 
  print('[+] end of main')

async def func(inp):
  print(f'[+] mana na vermisan got veran >>>{inp}')
  time.sleep(1)
  return inp+'_attached'

async def func1(inp):
  print('[+] func1 start')
  time.sleep(1)
  print('[+] func1 end')

async def func2():
  for i in range(10):
    print(f'[+] func2 : {i}')
    time.sleep(0.25)

asyncio.run(main())
