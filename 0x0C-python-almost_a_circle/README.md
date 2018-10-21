# 0x0C. Python - Almost a circle
---
## Description

This project in the High Level Programming series is about:
* Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Files
---
File|Task
---|---
models/base.py | A class called `Base` that other classes can inherit from
models/rectangle.py | A class called `Rectangle` that inherits from `Base`
models/square.py | A class called `Square` that inherits from `Rectangle`
models/\_\_init\_\_.py | Blank init file that makes the directory a module
tests/\_\_init\_\_.py | Blank init file that makes the directory a module
tests/test_models/\_\_init\_\_.py | Blank init file that makes the directory a module
tests/test_models/test_base.py | Contains test cases for `base.py`
tests/test_models/test_rectangle.py | Contains test cases for `rectangle.py`
tests/test_models/test_square.py | Contains test cases for `square.py`


## Directories
---
Directory Name | Description
---|---
main/ | Main files for all functions
tests/ | Contains a directory for testing models
tests/test_models/ | Contains all files that are used to test the models
models/ | Contains all the model files

## Author
Heindrick Cheung