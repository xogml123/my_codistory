n=int(input())
nums=list(map(int,input().split()))
sequence=[]
string=[]
result=0
left=0
right=n-1
if nums[left]<nums[right]:
    string.append('L')
    sequence.append(nums[left])
    left += 1
    result+=1

else:
    string.append('R')
    sequence.append(nums[right])
    right -= 1
    result+=1

while True:
    if left==right+1:
        break
    else:
        if sequence[-1]< nums[left] and sequence[-1]< nums[right]:

            if nums[left]<=nums[right]:
                string.append('L')
                sequence.append(nums[left])
                left+=1

                result+=1
            elif nums[left]>nums[right]:
                string.append('R')
                sequence.append(nums[right])
                right-=1

                result+=1


        elif sequence[-1]> nums[left] and sequence[-1]< nums[right]:
            string.append('R')
            sequence.append(nums[right])
            right -= 1

            result+=1
        elif sequence[-1]< nums[left] and sequence[-1]> nums[right]:
            string.append('L')
            sequence.append(nums[left])
            left += 1

            result+=1
        else:
            break
print(result)
print(''.join(string))