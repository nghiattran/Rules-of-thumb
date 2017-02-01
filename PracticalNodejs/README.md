# Practical Node.js

## Chapter 1

### Prototypal Nature

There are no * * classes* *  in JavaScript because objects inherit directly from other objects, which is called * * prototypal inheritance* * .

There are a few types of inheritance patterns in JavaScript:

* Classical
* Pseudoclassical
* Functional

### 1. Node.js Basics and Syntax

#### 1. Most common used funtions:

* Array
	* some() and every(): assertions for array items
	* join() and concat(): convertion to a string
	* pop(), push(), shift(), and unshift(): working with stacks and queues
	* map(): model mapping for array items
	* filter(): querying array items
	* sort(): ordering items
	* reduce(), reduceRight(): computing
	* slice(): copying
	* splice(): removing
	* indexOf(): lookups of finding the value in the array
	* reverse(): reversing the order
	* The in operator: iteration over array items
* Math
	* random(): random real number less than one
* String
	* substr() and substring(): extracting substrings
	* length: length of the string
	* indexOf(): index of finding the value in the string
	* split(): converting the string to an array

#### 2. Reading to and Writing from the File System in Node.js

Read

```js
	var fs = require('fs');
	var path = require('path');
	fs.readFile(path.join(__dirname, '/data/customers.csv'), {encoding: 'utf-8'}, function (err, data) {
		if (err) {
			throw err;
		}
		console.log(data);
	});
```

Write

```js 
	var fs = require('fs');
	fs.writeFile('message.txt', 'Hello World!', function (err) {
		if (err) throw err;
		console.log('Writing is done.');
	});
```

#### 3. Streaming Data in Node.js

Streaming data is a phrase that means an application processes the data while it’s still receiving it. Is useful for extra large datasets such as video or database migrations.

```js
	var fs = require('fs');
	fs.createReadStream('./data/customers.csv').pipe(process.stdout);
```

#### 4.Hello World Server with HTTP Node.js Module

```js
	var http = require('http');											
	http.createServer(function (req, res) {
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('Hello World\n');
	}).listen(1337, '127.0.0.1');
	console.log('Server running at http://127.0.0.1:1337/');
```

### 2. Debugging Node.js Programs

Debugging tools:

* Core Node.js Debugger: 

	A nongraphic user interface (non-GUI) minimalistic tool that works everywhere.

* Node Inspector: 

	Port of Google Chrome Developer Tools.

* WebStorm and other IDEs

#### 1. Core Node.js Debugger

```js
	var http = require('http');
	debugger;
	http.createServer(function (req, res) {
		res.writeHead(200, {'Content-Type': 'text/plain'});
		debugger;
		res.end('Hello World\n');
	}).listen(1337, '127.0.0.1');
	console.log('Server running at http://127.0.0.1:1337/');
```

* next, n: step to the next statement
* cont, c: continue until the next debugger/break point
* step, s: step inside the function call
* out, o: step outside the function call
* watch(expression): watch the expression

The full list of commands is available through the help command or on the official web site (http://nodejs.org/api/debugger.html).

#### 2. Debugging with Node Inspector

The built-in Node.js debugger client is extensive, but it’s not intuitive because of the lack of a GUI.

## Chapter 2: Using Express.js to Create Node.js Web Apps

### 1. How Express.js Works

The way routes are defined in Express.js is with helpers `app.VERB(url, fn1, fn2, ..., fn)`

#### Set routes

Where:

* `fnN` are request handlers
* `url` is on a URL pattern in RegExp, and 
* `VERB` values are as follows:

	* all: catch every request (all methods)
	* get: catch GET requests
	* post: catch POST requests
	* put: catch PUT requests
	* del: catch DELETE requests

#### Rendering pages

The `res.render(viewName, data, callback(error, html))` where parameters mean following:

	* `viewName`: a template name with filename extension or if view engine is set without the extension
	* `data`: an optional object that is passed as locals; for example, to use msg in Jade, we need to have {msg: "..."}
	* `callback`: an optional function that is called with an error and HTML when the compilation is complete

#### Start server

```js
http.createServer(app).listen(app.get('port'), function(){
	console.log('Express server listening on port ' + app.get('port'));
});
```

## Chapter 3: TDD and BDD for Node.js with Mocha

### Mocha Hooks

A **hook** is some logic, typically a function or a few statements, which is executed when the associated event happens.

Mocha provides some hooks like `before` and `beforeEach` hooks, there are `after()`, and `afterEach()`.

All hooks support asynchronous modes. The same is true for tests as well. For example, the following test suite is synchronous and won’t wait for the response to finish:

```js
	describe('homepage', function(){
		it('should respond to GET',function(){
			superagent
			.get('http://localhost:'+port)
			.end(function(res){
			expect(res.status).to.equal(200);
		})
	})
```

But we can add a done parameter to the test’s function and make it wait for response:

```
	describe('homepage', function(){
		it('should respond to GET',function(done){
			superagent
			.get('http://localhost:'+port)
			.end(function(res){
			expect(res.status).to.equal(200);
			done();
		})
	})
```

Test cases (`describe`) can be nested inside other test cases, and hooks such as before and beforeEach can be
mixed in with different test cases on different levels. Nesting of describe constructions is a good idea in large test files.

Sometimes, developers might want to skip a test case/suite (describe.skip() or it.skip()) or make them
exclusive (describe.only() or describe.only()). Exclusivity means that only that particular test runs (the
opposite of skip).

Tradition TDD interfaces:

* `suite`: analogous to describe
* `test`: analogous to it
* `setup`: analogous to before
* `teardown`: analogous to after
* `suiteSetup`: analogous to beforeEach
* `suiteTeardown`: analogous to afterEach

### TDD with the Assert

A sample tests:

```js
	var assert = require('assert');
	describe('String#split', function(){
		it('should return an array', function(){
			assert(Array.isArray('a,b,c'.split(',')));
		});

		it('should return the same array', function(){
			assert.equal(['a','b','c'].length, 'a,b,c'.split(',').length, 'arrays have equal length');
			for (var i=0; i<['a','b','c'].length; i++) {
				assert.equal(['a','b','c'][i], 'a,b,c'.split(',')[i], i + 'element is equal');
			};
		});
	})
```

Notice that we have some duplicates, duplicate can de reduced by using `beforeEach` and `before` constructions:

```js
	var assert = require('assert');
	var expected, current;
	before(function(){
		expected = ['a', 'b', 'c'];
	})
	describe('String#split', function(){
		beforeEach(function(){
			current = 'a,b,c'.split(',');
		})
		
		it('should return an array', function(){
			assert(Array.isArray(current));
		});

		it('should return the same array', function(){
			assert.equal(expected.length, current.length, 'arrays have equal length');
			for (var i=0; i<expected.length; i++) {
				assert.equal(expected[i], current[i], i + 'element is equal');
			}
		})
	})
```

## Chapter 4: Deploy

### Deploying to Amazon Web Services

* Clone from github
* Initial testing:
	* Create a simple node server.js
	* Redirect connections, or
	* Turn off firewall
```
	$ service iptables save
	$ service iptables stop
	$ chkconfig iptables off
```

### Keeping Node.js Apps Alive with forever, Upstart, and init.d

Luckily, there’s no shortage of solutions to monitor and restart our Node.js apps:
* forever (https://github.com/nodejitsu/forever): probably the easiest method. The forever module is installed via NPM and works on almost any Unix OS. Unfortunately, if the server itself fails (not our Node.js server, but the big Unix server), then nothing resumes forever.

* Upstart (http://upstart.ubuntu.com): the most recommended option. It solves the problem of starting daemons on startups, but it requires writing an Upstart script and having the latest Unix OS version support for it. We’ll show you an Upstart script example for CentOS.

* init.d (http://www.unix.com/man-page/opensolaris/4/init.d): an outdated analog of Upstart. init.d contains the last startup script options for systems that don’t have Upstart capabilities.

#### forever

Usage:

```sh
	$ sudo npm install forever –g
	$ forever server.js

	//or 

	$ forever start -l forever.log -o output.log -e error.log server.js
```

To stop the process, type:

```sh
	$ forever stop server.js
```

To look up all the programs run by forever, type:

```sh
	$ forever list
```

#### Upstart Scripts

**Upstart** is an event-based replacement for the /sbin/init daemon that handles starting of tasks and services during boot

http://upstart.ubuntu.com/getting-started.html