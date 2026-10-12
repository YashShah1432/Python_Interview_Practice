class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        student_collection = Counter(students)

        for sandwich in sandwiches:
            if student_collection[sandwich] > 0:
                student_collection[sandwich] -= 1
            else:
                break
        
        return sum(student_collection.values())