# Hashmap-Implementation

Welcome to my Hashmap Implementation!

## Table of Contents
  - [Overview](#overview)
  - [App File Structure](#app-file-structure)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation and Operation](#installation-and-operation)
## Overview

This implemenation contains 2 seperate files which contain the same functions but use different collision avoidance strategies - Open Addressing (OA) and Separate Chaining (SC). This project employs Continuous Integration Pipelining using Github Actions.

## App File Structure
The following is a brief overview of the file structure

[./hash_ma_oa.py](https://github.com/voyagerfan/Hashmap-Implementation/blob/main/hash_map_oa.py) - Hashmap functions that work with open addressing

[./hash_map_sc.py](https://github.com/voyagerfan/Hashmap-Implementation/blob/main/hash_map_sc.py) - Hashmap functions that work with separate chaining

[./a6_include.py](https://github.com/voyagerfan/Hashmap-Implementation/blob/main/a6_include.py) - Additional data structure classes to support building functions for separate chaining and open addressing

[./tests.py](https://github.com/voyagerfan/Hashmap-Implementation/blob/main/tests.py) - Testing suite for functions.

## Features

This project includes the following features:

* Two (2) separate hashmap classes that leverage collision avoidance strategies: Open Addressing and Separate chaining.
* Both files hash_map_sc.py and hash_map_oa.py have same functions.
  * **put**(self, key: str, value: object)
  * **table_load**(self) -> float
  * **empty_buckets**(self) -> int
  * **resize_table**(self, new_capacity: int) -> None
  * **get**(self, key: str) -> object
  * **contains_key**(self, key: str) -> bool
  * **remove**(self, key: str) -> None
  * **clear**(self) -> None
  * **get_keys_and_values**(self) -> DynamicArray
  * **__next__**(self)
* Github actions is used for Continuous integration pipelining.
  * Builds the project using the yml file.
  * lints the code
  * runs unit tests from tests.py


## Technologies Used

- **Programming Languages:** Python
- **Frameworks:** Unittest
- **Continuous Integration Platform:** Github Actions

## Installation and Operation

You may clone the repository and include it in your project file. Please make the appropriate imports for the functions you desire.

