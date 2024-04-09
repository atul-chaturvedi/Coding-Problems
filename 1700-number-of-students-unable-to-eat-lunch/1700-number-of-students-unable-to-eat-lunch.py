class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:        
        try:
            for sandwich in sandwiches:
                students.remove(sandwich)
        except:
            pass
        return len(students)
                
        