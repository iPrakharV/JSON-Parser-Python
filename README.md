# JSON Parser

This is a Python-based JSON parser that validates JSON objects. It checks for the correctness of the JSON format and handles multiple types of JSON structures, including strings, numbers, booleans, null values, arrays, and nested objects.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Tests](#tests)

## Introduction
This project helps you learn the basics of creating a simple JSON parser. The project consists of multiple steps:
- Step 1: Parsing an empty JSON object `{}`.
- Step 2: Parsing a simple key-value JSON object.
- Step 3: Parsing JSON with multiple types like strings, numbers, booleans, and null values.
- Step 4: Parsing nested objects and arrays.
- Step 5: Adding custom tests.

The parser uses Python’s built-in `json` module to validate JSON structures.

## Features
- Supports basic JSON object validation
- Handles JSON types: strings, numbers, booleans, nulls
- Supports nested objects and arrays
- Provides useful error messages for invalid JSON

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/iPrakharV/JSON-Parser-Python.git
    cd JSON-Parser
    ```

2. **Install Python**:
    Ensure that Python 3 is installed on your machine. You can download Python [here](https://www.python.org/downloads/).

## Usage

1. **Run the parser**:
    The main script takes a JSON object as input and determines whether it's valid or not.

    ```bash
    python parser.py
    ```

    After running the script, you'll be prompted to enter a JSON string, for example:

    ```
    Enter JSON data: {"key": "value"}
    ```

2. **Output**:
    The program will print either:
    - `Valid JSON Object`
    - `Invalid JSON Object` (with an error message if applicable)

## Examples

### Example 1: Valid JSON
```json
{
  "key1": true,
  "key2": false,
  "key3": null,
  "key4": "value",
  "key5": 101
}