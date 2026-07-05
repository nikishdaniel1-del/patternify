# My Package
A Python Package for generating Patterns.

## Installation
pip install patternify

## Usage Examples
### Example 1 - Square Pattern
```python
from patternify import square

print(square(5)) # normal pattern '*'
print(square(6,pattern='#')) # prints pattern with '#'
```
```
Output

*****
*****
*****
*****
*****

********
*######*
*######*
*######*
*######*
********

```
---

### Example 2 - Hollow Square Pattern
```python
from patternify import hollow_square

print(hollow_square(6,space='~'))
print(hollow_square(5,pattern='#',space='~'))
```
```
Output

*******
*~~~~~*
*~~~~~*
*~~~~~*
*~~~~~*
*******

#####
#~~~#
#~~~#
#~~~#
#####
```
---