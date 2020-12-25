I did part 1 with an list.  For part 2 I tried optimizing my list solution by eliminating index() calls by writing a function that iterated the whole list to store indexes.  This made things worse.  There's probably something I could have done there that might have worked but...  Then I tried converting my list to a deque which helped in some cases but not others. 

This is what I was dealing with:
...
Percent Complete: 0.2%
Starting iter 20000
Elapsed: 113.91210603713989
Iteration Delta: 87.14728593826294
Predicted overall completion Time: 15.821129109402674 hours
--------------------------------
--------------------------------
Percent Complete: 0.3%
Starting iter 30000
Elapsed: 282.91212916374207
Iteration Delta: 169.000009059906
Predicted overall completion Time: 26.195574461574186 hours
--------------------------------
--------------------------------
Percent Complete: 0.4%
Starting iter 40000
Elapsed: 513.4084439277649
Iteration Delta: 230.49627113342285
Predicted overall completion Time: 35.653369945604304 hours
--------------------------------
...
and only got much worse as time went on.

Ultimately I scratch wrote part 2 after poking around the reddit site.  At first I was pointing at class based linked lists; but then it became clear a dict of dict{cup:nextcup} made the most sense; and every move only included 3 'nextcup' changes.  And lookups were a non-iterative action. 

Ultimately got here:
--------------------------------
Percent Complete: 0.0%
Starting iter 0
Elapsed: 3.1948089599609375e-05
Iteration Delta: 4.6253204345703125e-05
--------------------------------
Percent Complete: 25.0%
Starting iter 2500000
Elapsed: 5.660773992538452
Iteration Delta: 5.660725116729736
--------------------------------
Percent Complete: 50.0%
Starting iter 5000000
Elapsed: 11.703214883804321
Iteration Delta: 6.042436122894287
--------------------------------
Percent Complete: 75.0%
Starting iter 7500000
Elapsed: 18.75826907157898
Iteration Delta: 7.055049896240234
--------------------------------
Percent Complete: 100.0%
Starting iter 10000000
Elapsed: 27.25309705734253
Iteration Delta: 8.494824886322021
The end
Just after one: 437752
Two after one: 12344
Result is: 5403610688


Live and learn.
