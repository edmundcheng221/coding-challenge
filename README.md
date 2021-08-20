# Documentation

To clone repo:

`git clone https://github.com/edmundcheng221/coding-challenge.git`


Run `fold.py`:

`python3 fold.py`

Run Unit Tests:
`python3 test_fold.py`


# Taktile Coding Challenge

Your challenge is to implement `fold` in the language of your choice.

## Description

`fold` is a higher order function that takes
* a sequence of type A
* a "starting" value of type B
* a function (A, B) -> B

and returns a B. E.g., the `sum` of an array is a special case of fold, where
* the sequence is an array of numbers
* the starting value is 0
* the function is `+`


You can find more information on [Wikipedia](https://en.wikipedia.org/wiki/Fold_(higher-order_function)).

## Instructions

Fork this repository.

Implement `fold` in any language of your choice. Don't directly use the `fold` that is
already part of your language (see the list on Wikipedia).

Send us a link to your fork **within 1 week** of being invited to participate on this challenge.

## Timebox

Aim to use about 1 hour of time on the solution, don't use more than 2 hours. We give roughly
equal weight to the each of the following:

* Documentation
* Packaging
* Testing
* Readability of code
* Correctness of implementation
* Performance
* Generality
* Correntness of types (if applicable)

Please don't stress if your solution isn't perfect. With a timebox of at most 2 hours, 
you most likely won't be able to check all the boxes above. This challenge is intended as an 
exercise in tradeoffs. We want to understand how you view the overall value and lifecycle
of software.

