# My Package
A Python Package for generating Patterns

## Installation
pip install patternify

## Example 1 - Square Pattern
```python
from patternify import square

print(square(5)) # normal pattern '*'
print(square(5,pattern='#')) # prints pattern with '#'
```

## Example 2 - Hollow Square Pattern
```python
from patternify import hollow_square

print(hollow_square(7,space='~'))
print(hollow_square(5,pattern='#',space='~'))
```