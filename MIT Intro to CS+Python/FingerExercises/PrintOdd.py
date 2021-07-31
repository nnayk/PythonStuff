#pg 24 finger exercise
first=int(input("Enter first number: "))
second=int(input("Enter first number: "))
third=int(input("Enter first number: "))
nums=[first,second,third]
max_odd=first
if nums[0]%2==0 and nums[1]%2==0 and nums[2]%2==0:
  print("There are no odd numbers in this list. The smallest number is "+str(min(nums)))
else:
  for x in nums:
      if x%2!=0 and x>max_odd:
        max_odd=x
  print("The largest odd number in this list is "+str(max_odd))

#first=second if second>third else third
#print("first="+str(first))
