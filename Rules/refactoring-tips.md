#Refactoring tips

1. **Refactoring** (noun): a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior.

2. When you find you have to add a feature to a program, and the program's code is not structured in a convenient way to add the feature, first refactor the program to make it easy to add the feature, then add the feature.

3. Before you start refactoring, check that you have a solid suite of tests. These tests must be self-checking.

4. Refactoring changes the programs in small steps. If you make a mistake, it is easy to find the bug.

5. Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

6. Make sure all tests are fully automatic and that they check their own results.

7. A suite of tests is a powerful bug detector that decapitates the time it takes to find bugs.

8. Run your tests frequently. Localize tests whenever you compile—every test at least every day.

9. When you get a bug report, start by writing a unit test that exposes the bug.

10. Don't forget to test that exceptions are raised when things are expected to go wrong.

11. Don't let the fear that testing can't catch all bugs stop you from writing the tests that will catch most bugs.