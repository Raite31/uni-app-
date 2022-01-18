#include <stdio.h>

int removeDuplicates(int* nums, int numsSize){
    if(numsSize==0){
        return 0;
    }
    int i = 0;
    int j = 1;
    for(j;j<numsSize;j++){
        if(nums[i]!=nums[j]){
            i = i + 1;
            nums[i] = nums[j];
        }
    }
    return i+1;
}

int removeDuplicates(int* nums, int numsSize){
    if(numsSize == 0){return 0;}
    int slow = 0, fast = 1;
    while(fast < numsSize){
        if(nums[fast] != nums[slow]){
            slow = slow + 1;
            nums[slow] = nums[fast];
        }
        fast = fast + 1;
    }
    return slow + 1;
}

Success
Details 
Runtime: 24 ms, faster than 23.66% of C online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 7.5 MB, less than 56.36% of C online submissions for Remove Duplicates from Sorted Array.