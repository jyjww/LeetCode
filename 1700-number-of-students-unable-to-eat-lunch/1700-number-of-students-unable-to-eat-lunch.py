class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQ = deque(students)
        count = 0
        i = 0

        while studentQ and count < len(studentQ):
            if studentQ[0] == sandwiches[i]:
                studentQ.popleft()
                i += 1 
                count = 0
            else:
                a = studentQ.popleft()
                studentQ.append(a)
                count += 1 
        return count
