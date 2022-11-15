class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:

        def islandCreator(stones: list[list[int]]) -> None:
            island = [stones.pop(0)]
            count = 0
            while count < len(island):
                stones_clone = stones[:]
                for stone in stones_clone:
                    if (stone[0] == island[count][0]) or (stone[1] == island[count][1]):
                        island.append(stone)
                        stones.remove(stone)
                count += 1

        total_stones = len(stones)
        island_count = 0
        while stones:
            islandCreator(stones)
            island_count += 1
        return total_stones - island_count


sol = Solution()
print(sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
