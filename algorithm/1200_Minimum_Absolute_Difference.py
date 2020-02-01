class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff_dict = {}
        m = float("inf")
        n = len(arr)
        for i in range(n - 1):
            if m >= (arr[i+1] - arr[i]):
                m = arr[i+1] - arr[i]
                if m not in diff_dict:
                    diff_dict[m] = [[arr[i], arr[i+1]]] 
                else:
                    diff_dict[m].append([arr[i], arr[i+1]])
                    
        return diff_dict[m]
