- Search problems:

    - Terminology:
        - Agent: perceives environment and acts upon it
        - State: configuration of the agent:
            - Initial state
        - Actions: choices made in a state:
            - Possibly valid in some state, but not in others
            - ACTIONS(s) -> actions valid for s
        - Transition model: what state we get after applying an action:
            - RESULTS(s, a) -> s'
            - State space:
                - Graph of states
        - Goal test: way to determine a state is the goal state
        - Path cost: numerical cost associated with a path

    - Node: datastructure keeping track of:
        - current state
        - parent node
        - action from parent node to get to this one
        - path cost

    - Approach:
        - start with initial state in the frontier
        - repeat:
            - if no action in frontier then no solution
            - take node from frontier
            - if node contains goal then return solution
            - expand node add results to frontier

    - Problems:
        - cycles. fix: keep set of explored states
        - how to pick from the frontier?:
            - Depth-First Search: stack (LIFO)
            - Breadth-First Search : queue (FIFO)

    - Informed and uninformed search
        - Uninformed: no problem specific info
        - Informed

    - Greedy DFS: explore cosest estimated by heuristic:
        - Manhantan heuristic

    - Adversarial search:
        - Minimax
            - Negative player 1 wins / Positive player 2 wins
            - Programming requirements
                - s0: initial state
                - player(s) -> who plays next
                - actions(s) -> possible actions
                - result(s, a) -> altered state
                - terminal(s) -> if the state is terminal
                - utility(s) -> provides the value of the state (such as def for min and max)
            - Principal
                - explore all state by switching users and compute the value given the possible linked outcomes
            - Algorithme
                - Each plays as if the opponent makes the optimal choice (= min or max value)
                - Optimization: alpha-betha pruning
                - Depth-limited minimax
                    - Evaluation function


https://video.cs50.io/WbzNRTTrX0g?screen=0Towr-pBuzw&start=1568
1'27'00 (first time)
