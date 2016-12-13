## Loop Analysis

#### 1. O(1)

No loop or loop variable is a constant number

#### 2. O(n)

Loop variable is variable and incremented / decremented by a constant number

```
for (int i = 1; i <= n; i += c) {  
  // some O(1) expressions
}
```

#### 3. O(n<sup>c</sup>)

Nested loops. O(n<sup>2</sup>) example:

```
for (int i = 1; i <=n; i += c) {
  for (int j = 1; j <=n; j += c) {
    // some O(1) expressions
  }
}  
```

#### 4. O(Logn)

Loop variables is divided / multiplied by a constant amount.

```
for (int i = 1; i <=n; i *= c) {
  // some O(1) expressions
}
```

#### 5. O(LogLogn)

Loop variables is reduced / increased exponentially by a constant amount.

```
for (int i = 2; i <=n; i = pow(i, c)) { 
  // some O(1) expressions
}
```

## Amortized Analysis Introduction

Amortized Analysis is used for algorithms where an occasional operation is very slow

## Space Complexity

**Auxiliary Space** is the extra space or temporary space used by an algorithm.

**Space Complexity** of an algorithm is total space taken by the algorithm with respect to the input size. Space complexity includes both Auxiliary space and space used by input.

## Pseudo-polynomial Algorithms

Pseudo-polynomial Algorithm: An algorithm whose worst case time complexity depends on numeric value of input (not number of inputs).

## NP-Completeness

## Searching and Sorting:

#### Minimum length of unsorted subarray

Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted.

Examples:
1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able to find that the subarray lies between the indexes 3 and 8.

2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find that the subarray lies between the indexes 2 and 5.


Solution O(n):
1) Find the candidate unsorted subarray 
a) Scan from left to right and find the first element which is greater than the next element. Let s be the index of such an element. In the above example 1, s is 3 (index of 30).
b) Scan from right to left and find the first element (first in right to left order) which is smaller than the next element (next in right to left order). Let e be the index of such an element. In the above example 1, e is 7 (index of 31).

2) Check whether sorting the candidate unsorted subarray makes the complete array sorted or not. If not, then include more elements in the subarray.
a) Find the minimum and maximum values in arr[s..e]. Let minimum and maximum values be min and max. min and max for [30, 25, 40, 32, 31] are 25 and 40 respectively.
b) Find the first element (if there is any) in arr[0..s-1] which is greater than min, change s to index of this element. There is no such element in above example 1.
c) Find the last element (if there is any) in arr[e+1..n-1] which is smaller than max, change e to index of this element. In the above example 1, e is changed to 8 (index of 35)

3) Print s and e.

Solution in Python

```python
def min_length_unsorted(nums):
    lowbound = -1
    highbound = -1

    for index in range(1,len(nums)):
        if nums[index] < nums[index-1] and (lowbound == -1 or lowbound > index - 1):
            lowbound = index - 1

    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1] and (highbound == -1 or highbound < index + 1):
            highbound = index + 1

    min_value = min(nums[lowbound: highbound + 1])
    max_value = max(nums[lowbound: highbound + 1])

    index = lowbound
    while index > 0:
        if nums[index - 1] > min_value:
            lowbound = index - 1
        index -= 1

    index = highbound
    while index < len(nums) - 1:
        if nums[index + 1] < max_value:
            highbound = index + 1
        index += 1

    return lowbound, highbound
```

#### k closest elements

Given a sorted array arr[] and a value X, find the k closest elements to X in arr[]. 
Examples:

```
Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
```

Solution:
1. Find index of the given integer using binary search O(logn)
2. Using 2 pointers: left and right to point to two closest indexes from the found index. if `value - nums[left] > nums[right] - value`, put the value at left into the ouput and move left point to the next left by one. Same thing for right pointer.

```python
def search(nums, value, start, end):
    if start > end:
        return -1

    mid = int((end + start) / 2)

    if nums[mid] == value:
        return mid
    elif nums[mid] > value:
        return search(nums, value, start, mid - 1)
    else:
        return search(nums, value, mid + 1, end)

def k_closet(nums, value ,k):
    output = []
    index = search(nums, value, 0, len(nums) - 1)

    if index == -1:
        return output

    right = index + 1
    left = index - 1
    for i in range(k):
        if right >= len(nums) or nums[right] - value > value - nums[left]:
            output.append(nums[left])
            left -= 1
        elif left < 0 or value - nums[left] > nums[right] - value:
            output.append(nums[right])
            right += 1
    return output
```

#### Sort n numbers in range from 0 to n^2 – 1 in linear time

Note: interesting problem

There are 3 basic algorithms for linear time sorting: counting sort, bucket sort, and radix sort but keep in mind they have certain requirements too.

**Counting sort** is not a solution for this since values ranging from 0 to n^2 - 1 so time complexity is `O(n^2)`.

**Bucket sort** is not a solution since notthing says about data distribution

**Radix sort** time complexity is `O(d*(n+b))`. Where: `b` is the base, 10 for decimal and `d` is hightest number of digits. In this case, the biggest value is n^2 - 1, `d` = log<sub>b</sub>(n^2). The trick is choosing base, `b`, so that `b` = `n`. Hence `d` = log<sub>b</sub>(n^2) = 2 and O(d*(n+b)) = O(log<sub>b</sub>(n^2)(n+b)) = O(log<sub>n</sub>(n^2)(n+n)) = O(2(2n)) = O(n).

By change base to n, all number in the given array would consist of 1 or 2 bits. Then we can perform Radix sort on those.

TODO: come back to this one

#include<iostream>
#include<climits>
using namespace std;
 
int partition(int arr[], int l, int r);
 
// This function returns k'th smallest element in arr[l..r] using
// QuickSort based method.  ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
int kthSmallest(int arr[], int l, int r, int k)
{
    // If k is smaller than number of elements in array
    if (k > 0 && k <= r - l + 1)
    {
        // Partition the array around last element and get
        // position of pivot element in sorted array
        int pos = partition(arr, l, r);
 
        // If position is same as k
        if (pos-l == k-1)
            return arr[pos];
        if (pos-l > k-1)  // If position is more, recur for left subarray
            return kthSmallest(arr, l, pos-1, k);
 
        // Else recur for right subarray
        return kthSmallest(arr, pos+1, r, k-pos+l-1);
    }
 
    // If k is more than number of elements in array
    return INT_MAX;
}
 
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
 
// Standard partition process of QuickSort().  It considers the last
// element as pivot and moves all smaller element to left of it
// and greater elements to right
int partition(int arr[], int l, int r)
{
    int x = arr[r], i = l;
    for (int j = l; j <= r - 1; j++)
    {
        if (arr[j] <= x)
        {
            swap(&arr[i], &arr[j]);
            i++;
        }
    }
    swap(&arr[i], &arr[r]);
    return i;
}
 
// Driver program to test above methods
int main()
{
    int arr[] = {12, 3, 5, 7, 4, 19, 26};
    int n = sizeof(arr)/sizeof(arr[0]), k = 3;
    cout << "K'th smallest element is " << kthSmallest(arr, 0, n-1, k);
    return 0;
}