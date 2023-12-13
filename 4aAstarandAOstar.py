from simpleai.search import SearchProblem, astar

goal = 'helloworld'

class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(goal):
            return list('abcdefghijklmnopqrstuvwxyz')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == goal

    def heuristic(self, state):
        wrong = sum([1 if state[i] != goal[i] else 0 for i in range(len(state))])
        missing = len(goal) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
result = astar(problem)
print(result.state)
print(result.path())


CMD COMMAND
1.pip install simpleai
2.pip install pydot flask




'''Explanation:
The A* (pronounced "A-star") algorithm is a popular and widely used path finding
algorithm in computer science and artificial intelligence. It is primarily used to find
the shortest path between two points on a graph or grid while efficiently exploring
the most promising nodes along the way. The A* algorithm combines the advantages
of a heuristic search.
The AO* algorithm is based on AND-OR graphs to break complex problems into
smaller ones and then solve them. The AND side of the graph represents those tasks
that need to be done with each other to reach the goal, while the OR side stands
alone for a single task'''
