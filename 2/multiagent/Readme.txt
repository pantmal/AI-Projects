I used the reciprocal of important values as it was noted in the assignment's presentation

Getting the Manhattan distances from Pacman's current position to the remaining food states

To get the result we need, this evaluation function returns our current score, plus the closest food, subtracting the closest ghost distance (so Pacman can avoid it), and we also add the closest capsule.  

#However if the ghosts are scared, there's no need to avoid them, so return the other values.

Max_Val is called for the states that Pacman is in

For every successor state, call the Min_Val function to get its value and return the action of the successor state with biggest value

the maximum value as well as the action that brings us to this node

is called for the ghost states
call the evaluation function to assign a value
If it is the last agent we have this means every other ghost has received its Minimax value so it's time to call Max_Val so Pacman may continue.  For every successor state, call the Max_Val function to get its value and return the action of the successor state with smallest value call Min_Val again because there are ghosts that haven't received their Minimax values

The algorithm is almost the exact same as in Minimax, only here the alpha and beta values are taken into account.
are passed in every function call
If the value of the succesor state is bigger than beta there's no need to explore the successors, so we prune them by returning the (v_node, next_action) tuple

The algorithm is almost the exact same as in Minimax, only here the Exp_Val function is defined for the ghost states.
The value we need is calculated by getting the average from the values of each successor state.

The evaluation function is quite similar to the one I implemented in the Reflex Agent. In this one, I decided to use max values since they provided better scores.
This evaluation function will return our current score as well as the max values we just calculated
