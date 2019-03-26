# Robot Navigation

We use runtime monitors constructed from formal specifications to enforce safety properties specified in temporal logic on-the-fly and guide them to perform their (navigational) tasks specified in regular expressions. 

## Examples

The first example illustates the basic obstacle avoidance of the robot in a convex freespace: 

![Alt Text](first.gif)

where the red dot is an (adversarial) agent and manually controlled via the keyboard to pose challenges to the robots performing their missions. Robots surely don't know our (red dot's) actions beforehand; therefore, they cannot plan thoroughly at design time. A game-theoretic approach would consider the worst case to solve the problem but we first need to answer a lot of questions and make a lot of assumptions: How do we know the worst case? What is the speed of the red dot? What about other dynamics? What if a purple dot comes in? etc.

Instead we took a reactive approach in these examples and act situations accordingly at runtime. At every time step, we consider a set of possible actions, obtain safe trajectories (in green), and select the best (in bold green) according to some heuristics. 

However, although short-horizon trajectory search are very effective, it can be stuck at local minima in non-convex free spaces. For these environments, we need to add a layer of graph search over the connectivity graph of the environment (passages that connects convex subsets and other features such as one-way regions). 

Similarly we can enforce safety properties on the graph search using runtime monitors. For example, the robot in the second video is instructed to NOT pass from the first door of the Room3 (top right room) while going from D to A. Therefore it follows a longer route using the second door below:

![Alt Text](second.gif)

Finally we present a complete example that includes four robots with different navigational missions in a non-convex environment with rules and regulations:

![Alt Text](final.gif)

The source code of this case study can be found in this directory.