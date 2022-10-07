# Learning Multi Threading and asyncio
## difference of threading and multi proccessing
- threads has common memory where as processes has seperate memories.
- However in multi threading you can end up in racing situation which threads are trying read and write to same data which causes unpredictable behavior.
- Also multi-threading programm is hard to understand. 
- They also introduce some overhead.
## asyncio 
- asyncio is a different story which relies on future, like promisses
- asyncio starts a function and does other things and whenever you need that function to be finished, you can call await. exactly like a boomerang
## issue:
- you cannot call you asyncio programm file ```asyncio```. [link](https://github.com/tornadoweb/tornado/issues/2868)
