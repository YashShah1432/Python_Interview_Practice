class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        count = 0
        for i in range(len(seats)):
            if students[i] > seats[i]:
                count += students[i] - seats[i]
            elif students[i] < seats[i]:
                count += seats[i] - students[i]
            else:
                continue
        return count