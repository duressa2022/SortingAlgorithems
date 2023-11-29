"""
 * DO NOT ALTER OR REMOVE THIS  NOTICES OR THIS FILE HEADER FROM THE CODE.
 * This code is free software you can redistribute it and/or modify it
   published by the Good will of the author.

 * This code is distributed in the hope that it will be useful,Therefore
   use this code for your need or purpose and you can inform Error or part
   to modify or add.
 * Modifiying this code in a part or as Whole is possible and incremental modification is
   suggested please inform the author any modification you have done.
 * Please contact the Author,if you need additional information or have any questions.
     *Author:Duressa Shukuri
     *Email:duressashukuri2022@gmail.com
"""
"""BUBBLESORT,
   SELECTION SORT,
   INSERTION SORT,
   MERGE SORT,
   QUICK SORT,
   HEAP SORT,
   COUNTING SORT,
   RADIX SORT,
   SHELL SORT"""
def functionBubbleSort(array,reverse=False):
    """
        This method sorts elements of the array by using bubble sorting algorithem
        works by continually exchanging tthe kneighboring elements of the array
        untill all elements of the array are sorted
        params: array,rev=False for increasing order sorting else False
        return: None
    """
    for i in range(len(array)):
        for j in range(len(array)-1):
            if not reverse:
                if array[j]>array[j+1]:
                    (array[j],array[j+1])=(array[j+1],array[j])
            else:
                if array[j]<array[j+1]:
                    (array[j],array[j+1])=(array[j+1],array[j])
def functionSelectionSort(array,reverse=False):
    """
       This method sorts elements of the array by using selection sorting algorithem
        works by selecting min or max elements of the array and putting it in correct position
        untill all elements of the array are sorted
        params: array,rev=False for increasing order sorting else False
        return: None
    """
    for i in range(len(array)):
        min=i,max=i
        for j in range(i+1,len(array)):
            if not reverse:
                if array[min]>array[j]:
                    min=j
            else:
                if array[max]<array[j]:
                    max=j
        if not reverse:(array[min],array[i])=(array[i],array[min])
        (array[max],array[i])=(array[i],array[max])
def functionInsertionSort(array,reverse=False):
    """
        This method sorts elements of the array by using inserting sorting algorithem
        which puts element on it correct position untill all elements of the array are sorted
        params: array,rev=False for increasing order sorting else False
        return: None
    """
    for i in range(len(array)):
        for j in range(i,0,-1):
            if not reverse:
                if array[j-1]>array[j]:
                    (array[j-1],array[j])=(array[j],array[j-1])
            else:
                if array[j-1]<array[j]:
                    (array[j-1],array[j])=(array[j],array[j-1])
def functionMergeSort(array):
    """
        This method sorts elements of the array by using mergeSort  algorithem
        which uses divide and conquer method inorder sort  elements of the array
        params: array
        return: None
    """
    def functionMerge(array1,array2,array):
        """
            This method merges elements of the array1 and array2 and helps as teping stone for mergeSort  algorithem
            params: array1, and array2 both of them must be sorted
            return: None
        """
        i=j=k=0
        while i<len(array1) and j<len(array2):
            if array1[i]<array2[j]:
                array[k]=array1[i]
                i=i+1
            else:
                array[k]=array2[j]
                j=j+1
            k=k+1
        while i<len(array1):
            array[k]=array1[i]
            i=i+1
            k=k+1
        while j<len(array2):
            array[k]=array[j]
            j=j+1
            k=k+1
    if len(array)<=1:
        return
    mid=len(array)//2
    left=functionMergeSort(array[:mid])
    right=functionMergeSort(array[mid:])
    functionMerge(left,right,array)
def functionQuickSort(array,low,high):
    """
       This method sorts elements of the array by using quickSort  algorithem
       which uses divide and conquer method inorder sort  elements of the array
       params: array,lower and higher interval of the element of the array
       return: None
    """
    def functionPartition(array,low,high):
        """
           This method partition elements of array based on hoares partition schema and helps as
           steping stone for QuickSort  algorithem
           params: array
           return: index of the pivot
        """
        pivot=array[high]
        i=low-1
        for j in range(low,high):
            if array[j]<pivot:
                i=i+1
                (array[i],array[j])=(array[j],array[i])
        (array[i+1],array[high])=(array[high],array[i+1])
        return i+1
    if low>=high:
        return
    pivot=functionPartition(array,low,high)
    functionQuickSort(array,low,pivot-1)
    functionQuickSort(array,pivot+1,high)
def functionHeapSort(array):
    """
        This method sorts elements of the array  by using heap datastucture(coverts array in to maxheap)
        by using other helper function
        params: array
        return: None
    """
    def functionHeapfiy(array,index,size):
        """
            This method heapfiy the element of the array that is given by index=index
            by using other helper function
            params: array,index,and size of array
            return: None
        """
        left=index*2+1
        right=index*2+2
        largest=index
        if left<size and array[left]>array[largest]:
            largest=left
        if right<size and array[right]>array[largest]:
            largest=right
        if index!=largest:
            (array[index],array[largest])=(array[largest],array[index])
            functionHeapfiy(array,largest,size)
    for i in range(len(array)//2-1,-1,-1):
        functionHeapfiy(array,i,len(array))
    for i in range(len(array)-1,0,-1):
        (array[0],array[i])=(array[i],array[0])
        functionHeapfiy(array,0,i)
def functionHeapSort(array):
    """
        This method sorts elements of the array  by using heap datastucture(coverts array int to minheap)
        by using other helper function
        params: array
        return: None
    """
    def functionHeapfiy(array,index,size):
        """
           This method heapfiy the element of the array that is given by index=index
           by using other helper function
           params: array,index,and size of array
            return: None
        """
        left=index*2+1
        right=index*2+2
        smallest=index
        if left<size and array[left]<array[smallest]:
            smallest=left
        if right<size and array[right]<array[smallest]:
            smallest=right
        if index!=smallest:
            (array[index],array[smallest])=(array[smallest],array[index])
            functionHeapfiy(array,index,size)
    for i in range(len(array)//2-1,-1,-1):
        functionHeapfiy(array,i,len(array))
    for i in range(len(array)-1,0,-1):
        (array[0],array[i])=(array[i],array[0])
        functionHeapfiy(array,0,i)
