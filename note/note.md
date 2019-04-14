* What is \_\_main\_\_ in python
  * '\_\_main\_\_' is the name of the scope in which top-level code executes. A module’s \_\_name\_\_ is set equal to '\_\_main\_\_' when read from standard input, a script, or from an interactive prompt.


* How-To python format()
  [how-to python format](https://www.geeksforgeeks.org/python-format-function/)

* Difference between `args` and `params`

  * A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters. Parameter is variable in the declaration of function. Argument is the actual value of this variable that gets passed to function

* Mutable and immutable

* ![mutable and immutable](/home/loveplay1983/WorkSpace/programming/Python/project/mdn_python_django_as_well_as_python_online_study/python_online_edu/note/mutable_immutable.png)

* ![mutable and immutable list](/home/loveplay1983/WorkSpace/programming/Python/project/mdn_python_django_as_well_as_python_online_study/python_online_edu/note/mutable_immutable_tbl.png) 

*  It is a little bit awkward to understand which one is mutable or immutable, hence a concrete example would be nice to put this on

  * mutable object like list, dict or set

    *  ```ipython
      In [42]: m = list([1, 3, 4])                                                                                                   
      
      In [43]: n = m                                                                                                                 
      
      In [44]: id(m) == id(n)                                                                                                        
      Out[44]: True
      
      In [45]: m.pop()                                                                                                               
      Out[45]: 4
      
      In [46]: id(m) == id(n)                                                                                                        
      Out[46]: True
      
      In [47]: n                                                                                                                     
      Out[47]: [1, 3]
      
      In [48]: m                                                                                                                     
      Out[48]: [1, 3]
      
       ```

    * both `n` and `m` points to the same list object as it was originally m and later assigned to n, after the pop() operation their id still remain the same as it was.

  * immutable object like string, int 

    * ```ipython
      In [36]: a = 1                                                                                                                 
      
      In [37]: b = a                                                                                                                 
      
      In [38]: id(a), id(b)                                                                                                          
      Out[38]: (94020215958048, 94020215958048)
      
      In [39]: a += 1                                                                                                              
      
      In [40]: a                                                                                                                     
      Out[40]: 2
      
      In [41]: id(a), id(b)                                                                                                          
      Out[41]: (94020215958080, 94020215958048)
      ```

    *  In the above code, `a` was originally assigned with 1 and later assigned `a` to `b`, therefore `b` equals `a`, at that time we have done it by `id()` method.

    * Then add 1 to `a`, a is changed but `b` still remain the same value since int is immutable.