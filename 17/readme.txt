Part 1:
--------------------------------
Starting iter 6
Elapsed: 570.3193759918213
Iteration Delta: 92.49025011062622
--------------------------------
Starting iteration, length of grid 10648
Starting iteration sum of 187
ending iteration, length of grid 10648
ending iteration sum of 368
mitskjs:17 kjsits$


So this probably not going to work for part 2



'refactored' part1 _eyeroll_
Starting iter 6
Elapsed: 492.96131205558777
Iteration Delta: 98.11849093437195
--------------------------------
ending iteration sum of 368



Best guess is refactor with dict index of tuple and stop doing the index lookup by value thing

(yes, slowdown was in lookup dict by value.  I never should have done it that way). 

I did the ugliest thing for part 2 with indexing the dict with a string joined tuple

--------------------------------
Starting iter 6
Elapsed: 166.99835515022278
Iteration Delta: 33.424257040023804
--------------------------------
Iteration total2696
