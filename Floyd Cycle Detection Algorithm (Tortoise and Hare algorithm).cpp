Floyd Cycle Detection Algorithm (Tortoise and Hare algorithm):

In order to detect cycles in any given singly linked list, we must set two pointers that traverse the data structure at different speeds. If they meet, we can determine that the list was circular. Then if we set the first pointer back to the head and slow them both down to the same speed, the next time they will meet will be the point where the node started pointing backward. The pseudo-code is as follows:

1. Initialize two pointers (tortoise and hare) that both point to the head of the linked list
2. Loop as long as the hare does not reach null
3. Set tortoise to next node
4. Set hare to next, next node
5. If they are at the same node, reset the tortoise back to the head.
6. Have both tortoise and hare both move one node at a time until they meet again
7. Return the node in which they meet
8. Else, if the hare reaches null, then return null

Big O
The time complexity of this algorithm is linear: O(n).
The space complexity of this algorithm is constant: O(1).


Exampler Problems:

Q1-Happy Number
A number is called happy if it leads to 1 after a sequence of steps wherein each step number is replaced by the sum of squares of its digit that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1.

Code-

// C/C++ program to check a number is a Happy 
// number or not 
#include <bits/stdc++.h> 
using namespace std; 

// Utility method to return sum of square of 
// digit of n 
int numSquareSum(int n) 
{ 
	int squareSum = 0; 
	while (n) 
	{ 
		squareSum += (n % 10) * (n % 10); 
		n /= 10; 
	} 
	return squareSum; 
} 

// method return true if n is Happy number 
bool isHappynumber(int n) 
{ 
	int slow, fast; 

	// initialize slow and fast by n 
	slow = fast = n; 
	do
	{ 
		// move slow number by one iteration 
		slow = numSquareSum(slow); 

		// move fast number by two iteration 
		fast = numSquareSum(numSquareSum(fast)); 

	} 
	while (slow != fast); 

	// if both number meet at 1, then return true 
	return (slow == 1); 
} 

// Driver code to test above methods 
int main() 
{ 
	int n = 13; 
	if (isHappynumber(n)) 
		cout << n << " is a Happy number\n"; 
	else
		cout << n << " is not a Happy number\n"; 
} 



Q2- Find the duplicate number.
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

code-

public class Solution {
    public int findDuplicate(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return -1;
        }    

    int slow = 0;
    int fast = 0;
    int finder = 0;

    while (true)
    {
        slow = nums[slow];
        fast = nums[nums[fast]];

        if (slow == fast)
            break;
    }
    while (true)
    {
        slow = nums[slow];
        finder = nums[finder];
        if (slow == finder)
            return slow;
    }
    }
}
