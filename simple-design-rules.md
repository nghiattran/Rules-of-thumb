#Kent Beck’s four rules of Simple Design
* [Runs all the tests](#tests)
* [Contains no duplication](#duplication)
* [Expresses the intent of the programmer](#express)
* [Minimizes the number of classes and methods](#minimize)



###1. <a name="tests"></a>Runs all the tests

Making our systems testable pushes us toward a design where our classes are small and single purpose. The more tests we write, the more we’ll continue to push toward things that are simpler to test. So making sure our system is fully testable helps us create better designs.

#####Writing tests leads to better designs.
#####Having tests eliminates the fear that cleaning up the code will break it!

We can increase cohesion, decrease coupling, separate concerns, modularize system concerns, shrink our functions and classes, choose better names, and so on. This is also where we apply the final three rules of simple design: Eliminate duplication, ensure expressiveness, and minimize the number of classes and methods.

###2. <a name="duplication"></a>Contains no duplication

Duplication is the primary enemy of a well-designed system. It represents additional work, additional risk, and additional unnecessary complexity.

###3. <a name="express"></a>Expresses the intent of the programmer

It’s easy to write code that we understand, because at the time we write it we’re deep in an understanding of the problem we’re trying to solve. Other maintainers of the code aren’t going to have so deep an understanding. So choose better names, split large functions into smaller functions, and generally just take care of what you’ve created. Care is a precious resource.

###4. <a name="minimize"></a>Minimizes the number of classes and methods


##Glossary
The **Single Responsibility Principle** (**SRP**) states that a class or module should have one, and only one, reason to change

By minimizing coupling in this way, our classes adhere to another class design principle known as the **Dependency Inversion Principle** (**DIP**).

The **Open/closed principle** (**OCP**) states "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification."