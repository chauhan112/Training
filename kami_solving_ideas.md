# steps:
  1. neighbour extract
      * use rectangular split method - done
      * use contour method - done
      * use triangular coordinate system 
  3. solve

## Solving strategy
* hypothesis testing
  * make neighbour network to tree form:- extract knowledge from this  (done)
  * maximum number of neighbour:- eg: the more number of neighbour a object has the better chance it has to combine all together
  * if a color connects all object of same color it must be right step:- argument: we need more than one step to delete the information i.e remove the structure. 
     So it the color connects all the objects with same color it must be the minimum step. however the order inwhich it should be done is still not clear yet.
  * same color object common neighbour:- Eg: if a particular object connect all the objects of same color, then it take precedence.
* make the brute force strategy
  * find the path of maximum gradient descent

## Hypothesis test

1. Nebor network
    * depth is always less than total number of steps
2. Max nebor: I think this hypothesis is already contained in the nebor tree. Because with the nebor tree, we can be sure that the given root has least depth,
    in other words, the given root combines every segments quickly. So whether the root is big or small does not matter as long as it combines all the segment.

## more
* detect the relation and color encoding without defining color
