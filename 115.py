#! /usr/bin/env python
#coding=utf-8
'''def process(num):
    # filter out non-evens
    if num % 2 != 0:
        return
    num = num * 3
    num = 'The Number: %s' % num
    return num
 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
for num in nums:
    print process(num)
 '''

'''Python的关键字 yield，这个关键字主要是返回一个Generator，
yield 是一个类似 return 的关键字，只是这个函数返回的是个Generator-生成器。
所谓生成器的意思是，yield返回的是一个可迭代的对象，并没有真正的执行函数。
也就是说，只有其返回的迭代对象被真正迭代时，yield函数才会正真的运行，
运行到yield语句时就会停住，然后等下一次的迭代。
'''
'''
    def even_filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num
def multiply_by_three(nums):
    for num in nums:
        yield num * 3
def convert_to_string(nums):
    for num in nums:
        yield 'The Number: %s' % num
 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(multiply_by_three(even_filter(nums)))
for num in pipeline:
    print num

'''
def even_filter(nums):
    return filter(lambda x: x%2==0, nums)
 
def multiply_by_three(nums):
    return map(lambda x: x*3, nums)
 
def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)
 
def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a), fns, data)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pipeline = pipeline_func(nums, [even_filter,
                     multiply_by_three,
                     convert_to_string])

'''pipeline = convert_to_string(
               multiply_by_three(
                   even_filter(nums)
               )
            )'''
for num in pipeline:
    print num
