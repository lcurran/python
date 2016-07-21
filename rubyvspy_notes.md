Lecture notes

Statically typed: type of variable is known at compile time (Java, C, C++)

Dynamically typed: the type of a variable is interpreted at runtime. This means that
you as a programmer can write a little quicker because you do not have to specify
type everytime. Example: Perl, Ruby, Python

Python vs ruby
https://www.upguard.com/articles/python-vs-ruby
http://dpk.io/pyvsrb

outwardly, they can seem very similar.  Both back end only, both very semantic
and easy to read.

However, they have some particular differences.  Ruby likes to have more than
one way of doing the same thing.

Python is a little more conservative. The zen of python states that there should
be only one optimal way to do something.  Thus python is more strict with layout
and formatting, because in python whitespace is considered syntax. (like tina said
yesterday). So for example any indented blocks have to all be the same number of
spaces.

"RoR relies heavily on "coding by convention" and "magic" that goes with that
convention, whereas Django relies on the Python motto "explicit is better than
implicit," and eschews magic."

these differences have resulted in a kind of ruby vs python war, since ruby violates
pretty much all of the zen of python, and ruby fans find python to be too rigid or
inflexible

> import this (print zen of python)

Ruby:
Use of blocks (blocks are essentially syntactic sugar for lambda, pythons way to
create anonymous functions, and read a lot better. also python lambdas can only
contain one expression)

Fragmentation (ruby libraries are much faster at offering support for new iterations
of the language, whereas a lot of python libraries still do not support python 3)

Hashable/ unhashable types(Ruby lets you call hash on anything, regardless of whether
it really makes sense to use it as a hash key; this allows it to be used to speed up
comparisons. Python only allows it to be used on immutable data types, which kind of
makes sense, but really makes assumptions which are not always guaranteed to be true)

Mutable strings(in python a string cannot be altered once it is assigned)

Python:
Better namespace handling and use of modules (each file has its own namespace and you
have to specifically import each module you want to use in a file, and you can rename
modules in each file to avoid namespace collisions, whereas ruby uses the convention
of putting everything in classes and modules in the hope that that will prevent
namespace collisions)

Central use of iterators(python can use for _ in to iterate over pretty much any
container object, and they are a central part of the language)

Internal functions (The idea being that you can nest defs to define functions that can only be used within the scope of another, enclosing function)

A richer set of data structures (builtin sets, tuples,)
