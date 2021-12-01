import asyncio

async def my_coroutine():
    print(42)

asyncio.run(my_coroutine())
# def my_generator():
#     a = 0
#     while a < 5:
#         yield a
#         a += 1
#
# class MyIterator:
#
#     def __iter__(self):
#         self.counter = 0
#         return self
#
#     def __next__(self):
#         if self.counter == 0:
#             self.counter += 1
#             return 42
#         else:
#             raise StopIteration
#
#
# for item in my_generator():
#     print(item)