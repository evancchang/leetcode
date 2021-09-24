class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        key = [0]
        
        while key:
            room = key.pop()
            if room not in visited:
                visited.add(room)
                key.extend(rooms[room])
            
        return len(visited) == len(rooms)
        
