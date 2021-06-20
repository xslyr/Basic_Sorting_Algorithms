#!/usr/bin/python3
# encoding utf-8

# BubbleSort Algorithm
#   Step 1 - Step Starting with the first element(index = 0), compare the current element with the next element of the array.
#   Step 2 - If the current element is greater than the next element of the array, swap them.
#   Step 3 - If the current element is less than the next element, move to the next element. 
#   Step 4 - Repeat Steps 1,2,and 3 until no exchange occurs.

 
import random, time

def BubbleSort(alist, verbose):
    task_completed = False
    while not task_completed:
        task_completed = True
        for id,item in enumerate(alist):
            try:
                if verbose : print('Is {} greater than {} ?'.format(alist[id], alist[id+1]))
                if alist[id] > alist[id+1]:
                    task_completed = False
                    if verbose : print(' - Changing alist[{}] = {} by alist[{}] = {}'.format(id,alist[id],id+1,alist[id+1]))
                    alist[id], alist[id+1] = alist[id+1], alist[id]
                    if verbose : print('{}'.format(alist))
            except:
                pass
    return alist

if __name__=='__main__':
    try:
        list_length = input('Input the list length : ')
        my_cluttered_list = list(range(int(list_length)))
        random.shuffle(my_cluttered_list)
        print(my_cluttered_list)
        verbose_question = input('Do you want print the BubbleSort steps? [ y / n ] : ')
        verbose = True if verbose_question.upper() == 'Y' else False
        print('Starting BubbleSort() ...')
        start = time.perf_counter()
        my_ordered_list = BubbleSort(my_cluttered_list, verbose)
        print('\nMy final ordered list is {} '.format(my_ordered_list))
        print('Task executed in {} seconds.\n'.format(time.perf_counter()-start))
    except Exception as e:
        print( e.message if hasattr(e,'message') else e )