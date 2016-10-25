# assignment-7
Predicative Parsing Table

1. Given the following CFG and the Predictive Parsing table. Write a program to trace input strings. Show the content of the stack after each match.
  1. (i+i)*i$
  2. i*(i-i)$
  3. i(i+i)$

2. Similar to problem #1, 
  1. remove left recursive grammars
  2. find the members of FIRST and FOLLOW and complete the following table
  3. construct the predictive parsing table, and write a program to trace input statements
    1. a=(a+a)*b$
    2. a=a*(b+a)$
    3. a=(a+a)b$
  
  
  ---
  
## Results using Main.py

Problem 1) 
  1. (i+i)*i$ => Valid
  2. i*(i-i)$ => Valid
  3. i(i+i)$ => Invalid
  
Problem 2)
  1. a=(a+a)*b$ => Invalid
  2. a=a*(b+a)$ => Invalid
  3. a=(a+a)b$ => Invalid
  
\- Weffe
