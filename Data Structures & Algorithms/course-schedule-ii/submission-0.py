class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = collections.defaultdict(list)
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            pre_map[pre].append(crs)
            in_degree[crs] += 1

        q = collections.deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        courses_order = []

        while q:
            current_course = q.popleft()
            courses_order.append(current_course)

            for neighbor in pre_map[current_course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return courses_order if len(courses_order) == numCourses else []
            
            