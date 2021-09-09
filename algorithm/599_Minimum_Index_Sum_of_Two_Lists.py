class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {}
        list2_map = {}
        common_list_map = {}
        
        for i, list in enumerate(list1):
            list1_map[list] = i
            
        for i, list in enumerate(list2):
            list2_map[list] = i
        
        for k, v in list1_map.items():
            if k in list2_map:
                idx_sum = v + list2_map[k]
                
                if idx_sum not in common_list_map:
                    common_list_map[idx_sum] = [k]
                else:
                    common_list_map[idx_sum].append(k)
                    
        min_idx = float('inf')
        for k, v in common_list_map.items():
            min_idx = min(min_idx, k)
            
        if min_idx == float('inf'):
            return []
        else:
            return common_list_map[min_idx]
