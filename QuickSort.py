#!/usr/bin/python3
# encoding utf-8

# QuickSort Algorithm - http://www.btechsmartclass.com/data_structures/quick-sort.html
#
#   Step 1 - Consider the first element of the list as pivot (i.e., Element at first position in the list).
#   Step 2 - Define two variables i and j. Set i and j to first and last elements of the list respectively.
#   Step 3 - Increment i until list[i] > pivot then stop.
#   Step 4 - Decrement j until list[j] < pivot then stop.
#   Step 5 - If i < j then exchange list[i] and list[j].
#   Step 6 - Repeat steps 3,4 & 5 until i > j.
#   Step 7 - Exchange the pivot element with list[j] element.
#

import random, time

def QuickSort(alist, first, last, verbose=False):
    if first < last : 
        _pivot = first
        _fst = first
        _lst = last
        if verbose: print('_fst: {} \t_lst: {}'.format(first,last))    
        while ( _fst < _lst ):
            while ( (alist[_fst] < alist[_pivot]) and _fst < last ): 
                if verbose: print(' Incrementing _fst to {}'.format(_fst+1))
                _fst+=1
            while (alist[_lst] > alist[_pivot] and _lst > first ): 
                if verbose: print(' Decrementing _lst to {}'.format(_lst-1))
                _lst-=1
            if _fst < _lst :
                if verbose: print(' Changing {} by {}'.format(alist[_fst], alist[_lst]))
                _aux = alist[_fst]
                alist[_fst] = alist[_lst]
                alist[_lst] = _aux
                if verbose: print(alist)

        if verbose: print(' Changing {} by {}'.format(alist[_pivot], alist[_lst]))
        _aux = alist[_pivot]
        alist[_pivot] = alist[_lst]
        alist[_lst] = _aux
        if verbose: print(alist)
        if _lst-1 >= 0: QuickSort(alist,first, _lst-1, verbose)
        if _lst+1 <= last: QuickSort(alist,_lst+1, last, verbose)
    return alist

if __name__ == '__main__':
    try:
        list_length = input('Input the list length : ')
        my_cluttered_list = list(range(int(list_length)))
        random.shuffle(my_cluttered_list)
        print(my_cluttered_list)
        verbose_question = input('Do you want print the QuickSort steps? [ y / n ] : ')
        verbose = True if verbose_question.upper() == 'Y' else False 
        print('Starting QuickSort() ...')
        start = time.perf_counter()
        my_ordered_list = QuickSort(my_cluttered_list, 0, len(my_cluttered_list)-1, verbose)
        print('\nMy final ordered list is {} '.format(my_ordered_list))
        print('Task executed in {} seconds.\n'.format(time.perf_counter()-start))
    except Exception as e:
        print( e.message if hasattr(e,'message') else e )