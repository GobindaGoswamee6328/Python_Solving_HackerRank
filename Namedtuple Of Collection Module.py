
from collections import namedtuple

(n, categories) = (int(input()), input().split())
Grade = namedtuple('Grade', categories)

marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))
