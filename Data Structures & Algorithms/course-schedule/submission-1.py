class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            in_degree[crs] += 1

        q = collections.deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        completed_courses = 0

        while q:
            current_course = q.popleft()
            completed_courses += 1

            for neighbor in preMap[current_course]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return completed_courses == numCourses