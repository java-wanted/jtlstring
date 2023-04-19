# jtlstring
A solution of of a two-letter string problem.

## TASK

  The task is stated by a high society commerce java senior.

```java
There are two-letter strings, 'AA', 'AB' and 'BB', which appear AB, AB and BB
times respectevely. The task is to join some of these strings to create the
longest possible string which does not contain 'AAA' or 'BBB'.

Write a function:
  String solution(int AA, int AB, int BB)
that, given three integers AA, AB and BB, returns the longest string that can
be createdaccording to the rules described above. If there is more than one
possible answer, the function may return any of them.

Examples:
- Given AA = 5, AB = 0 and BB = 2, the function should return 'AABBAABBAA'.
- Given AA = 1, AB = 2 and BB = 1, possible results are 'BBABABAA',
  'ABAABBAB', 'ABABAABB' or 'AABBABAB'.
- Given AA = 0, AB = 2 and BB = 0, the function should return 'ABAB'.
- Given AA = 0, AB = 0 and BB = 10, the function should return 'BB'.
```

## SOLUTION

Let there is an operation to solve the task:
- Let string start with some two-letter item, may be empty.
- There are up to three possibilities to add the next item, dependent on the
  last one and counters.
- For each possibilities use this operation to append a longest string,
  and return the longest resulting string.
- Of course, on each call to the operation a counter is decremented.

```c
; Find the longest two-letter string
jtlstring(string, counters)
    for each non zero counter
      if it is possible to append the related item
         call jtlstring(string + item, counters decremented)
    return the longest of strings
```

Indeed, an iterative implementation must be provided.

## AUTHOR

  Boris Stankevich <microsoft-wanted@yandex.ru>.

## LICENSE

  This project can be used in accordance with rules and limitation of
  License GPLv3+: GNU GPL version 3 or later
  <https://gnu.org/licenses/gpl.html>.

  This is free software: you are free to change and redistribute it.
  There is NO WARRANTY, to the extent permitted by law.
