import random, time

def BubbleSort(alist, verbose):
    task_completed = False
    while not task_completed:
        task_completed = True
        for id,item in enumerate(alist):
            try:
                if verbose == 'Y': print('{} > {} ?'.format(alist[id], alist[id+1]))
                if alist[id] > alist[id+1]:
                    task_completed = False
                    if verbose == 'Y': print(' - aux = {}'.format(item))
                    aux = item
                    if verbose == 'Y': print(' - alist[id] = {}'.format(alist[id+1]))
                    alist[id] = alist[id+1]
                    if verbose == 'Y': print(' - alist[id+1] = {}'.format(aux))
                    alist[id+1] = aux
                    if verbose == 'Y': print('{}'.format(alist))
            except:
                pass

    return alist

if __name__=='__main__':
    try:
        list_length = input('Input the list length : ')
        my_cluttered_list = list(range(int(list_length)))
        random.shuffle(my_cluttered_list)
        print(my_cluttered_list)
        verbose = input('Do you want print the BubbleSort steps? [ y / n ] : ')
        print('Starting BubbleSort() ...')
        start = time.perf_counter()
        my_ordered_list = BubbleSort(my_cluttered_list, verbose.upper())
        print('\nMy final ordered list is {} '.format(my_ordered_list))
        print('Task executed in {} seconds.\n'.format(time.perf_counter()-start))
    except Exception as e:
        print( e.message if hasattr(e,'message') else e )