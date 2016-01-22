# F.I.S.R.T rules for clean tests
###Fast 
Tests should be fast. They should run quickly. When tests run slow, you won’t want to run them frequently. If you don’t run them frequently, you won’t ﬁnd problems early enough to ﬁx them easily. You won’t feel as free to clean up the code. Eventually the code will begin to rot.
###Independent
Tests should not depend on each other. One test should not set up the conditions for the next test. You should be able to run each test independently and run the tests in any order you like. When tests depend on each other, then the ﬁrst one to fail causes a cascade of downstream failures, making diagnosis difﬁcult and hiding downstream defects.
###Repeatable
Tests should be repeatable in any environment. You should be able to run the tests in the production environment, in the QA environment, and on your laptop while riding home on the train without a network. If your tests aren’t repeatable in any environment, then you’ll always have an excuse for why they fail. You’ll also ﬁnd yourself unable to run the tests when the environment isn’t available.
###Self-Validating
The tests should have a boolean output. Either they pass or fail. You should not have to read through a log ﬁle to tell whether the tests pass. You should not have to manually compare two different text ﬁles to see whether the tests pass. If the tests aren’t self-validating, then failure can become subjective and running the tests can require a long manual evaluation.
###Timely
The tests need to be written in a timely fashion. Unit tests should be written just before the production code that makes them pass. If you write tests after the production code, then you may ﬁnd the production code to be hard to test. You may decide that some production code is too hard to test. You may not design the production code to be testable.

