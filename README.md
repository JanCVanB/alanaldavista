# AlanAldaVista

PageRank calculation using Amazon Elastic MapReduce (for Caltech Winter 2015 CS144)

Future students of CS144 should **NOT** view the contents of this repository or read below this point. Doing so is a direct violation of the honor code.


## Algorithm Pseudocode (using Amazon EMR)

<img src="http://i.imgur.com/YxxoCRX.gif" alt="Alan Alda pseudocoding" width="300" align="right"/>

<img src="http://i.imgur.com/5h110bY.png" alt="PageRank Map" width="400"/>

<img src="http://i.imgur.com/Pu0glZc.png" alt="PageRank Reduce" width="400"/>

<img src="http://i.imgur.com/Bs44Zsz.png" alt="Process Reduce" width="400"/>


## Approach

We adopted an Occam’s Razor approach to the problem: more complicated solutions may ultimately prove correct, but the fewer assumptions the better.

Because the data sets for processing were not known in advance, no assumptions about structure were possible and without any such knowledge it was difficult to optimize to take advantage of any specific characteristics of the network graph.

Additionally, the page-ranking computation and map-reduce functions scaled in operations linearly. This was a valuable characteristic that we sought to preserve in the algorithm. For this reason, complicated optimizations were omitted in preference for Pythonic improvements in the code, which would give operational benefits instead of algorithmic benefits.

Tolerance checks to determine the number of iterations were also omitted by relying on a property of convergence defined by the degree of desired error (discussed below). Avoiding a check for tolerance allowed the program to avoid costly computations in sorting which contributed to an optimized run-time. 


## Technical Considerations

One of the important questions under consideration was “how close to the final PageRanks does the algorithm have to get before the top twenty nodes are in order?” In other words, what degree of error from the true page ranks is tolerable with respect to obtaining an accurate ranking?

To answer this question, the team turned to the heavy-tailed property of network graphs. According to this framework, the page ranks of the nodes would follow a heavy tailed distribution that would obey the “catastrophe principle” - the page rank of the graph would be distributed in much higher concentrations in the higher ranked nodes than would be found in the lower ranked nodes.

Since the order of magnitude of the page ranks of the top twenty nodes would be on the order of 1 or larger, the team concluded that an error of 0.01 (from the final PageRanks) would be sufficient to correctly rank the top twenty nodes as this produces a negligible relative error in the page ranks of the top twenty nodes.

Since the number of iterations executed before declaring convergence partly determines the run time of the program, the natural follow-up question is, “how many iterations are required to obtain an error of 0.01?” Fortunately this question is answered by the following equation: convergence iteration = log(error) / log(alpha).

In the project guideline, alpha is specified as 0.85, so the convergence iteration is about 15.


## Contributions

<img src="http://i.imgur.com/uhg9IrV.gif" alt="Alan Alda contributing" width="300" align="right"/>

### Sean Dolan

- Implemented and debugged algorithm in Python
- Provided insight on the convergence iteration approximation
- Implemented optimizations proposed in brainstorming sessions

### Jan Van Bruggen

- Responsible for testing the program
- Implemented several testing scripts and procedures in Python
- Tested procedures and scripts both locally and remotely on AWS
- Participated in writing and debugging code

### Brad Chattergoon

- Assisted in developing the algorithm
- Participated in brainstorming sessions
- Researched potential optimization implementations for the algorithm
- Took lead on constructing the project report
