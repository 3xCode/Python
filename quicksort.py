def quicksort(a,left,right):
	key = a[left];
	while left<right:
		while a[right]>=key and left<right:
			right-=1;
		a[left]=a[right];

		while a[left]<=key and left<right:
			left+=1;
		a[right]=a[left];
		a[left]=key;
	print(a);
	return right;

def sort(a,left,right):
	if left>=right:
		return;
	index = quicksort(a,left,right);
	sort(a,left,index-1);
	sort(a,index+1,right);

if __name__ == '__main__':
	a=[6,2,3,12,5];
	sort(a,0,len(a)-1);