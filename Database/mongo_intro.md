# Data types

| Type                    | Number | Alias                 | Notes       |
|-------------------------|--------|-----------------------|-------------|
| Double                  | 1      | “double”              |             |
| String                  | 2      | “string”              |             |
| Object                  | 3      | “object”              |             |
| Array                   | 4      | “array”               |             |
| Binary data             | 5      | “binData”             |             |
| Undefined               | 6      | “undefined”           | Deprecated. |
| Object id               | 7      | “objectId”            |             |
| Boolean                 | 8      | “bool”                |             |
| Date                    | 9      | “date”                |             |
| Null                    | 10     | “null”                |             |
| Regular Expression      | 11     | “regex”               |             |
| DBPointer               | 12     | “dbPointer”           |             |
| JavaScript              | 13     | “javascript”          |             |
| Symbol                  | 14     | “symbol”              |             |
| JavaScript (with scope) | 15     | “javascriptWithScope” |             |
| 32-bit integer          | 16     | “int”                 |             |
| Timestamp               | 17     | “timestamp”           |             |
| 64-bit integer          | 18     | “long”                |             |
| Min key                 | -1     | “minKey”              |             |
| Max key                 | 127    | “maxKey”              |             |

# ObjectId format

ObjectIds use 12 bytes of storage, which gives them a string representation that is 24
hexadecimal digits: 2 digits for each byte. 

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|----|----|
|`Timestamp`|||`Machine`|||`PID`|||`Increment`|||

# Array modifiers

### Adding

##### Adding one with $push

````
    {
        '$push': {
            'array': {
                array_element
            }
        }
    }
````

##### Adding many with $each

````
    {
        '$push': {
            'array': {
                '$each': [array_element,array_element,array_element],
            }
        }
    }
````

##### Keep array length with $slice

`$slice` value must be negative. Keeping the last pushed items

````
    {
        '$push': {
            'array': {
                '$each': [array_element,array_element,array_element],
                '$slice' : -10
            }
        }
    }
````
##### Sorting before slice

Possible sorts (`value`) are 1 (for ascending) and −1 (for descending).

````
    {
        '$push': {
            'array': {
                '$each': [array_element,array_element,array_element],
                '$slice': -10,
                '$sort': {array_value: value}
            }
        }
    }
````

###### P/S: 
Note that you must include "$each"; you cannot just "$slice" or "$sort" an array with "$push".

##### Prevent duplications with $ne and $addToSet

```
    {
        "$addToSet" : {
            "emails" : "joe@gmail.com"
        }
    }
```

`$addToSet` can be used with `$each`

```
    {
        "$addToSet" : {
            "emails" : {
                "$each" :["joe@php.net", "joe@example.com", "joe@python.org"]
            }
        }
    }
```

##### Removing elements with $pop, $pull

`$pop` treats array as a queue. `key` takes 1 (poping from the end of array) and -1.

```
     {"$pop" : {"key" : 1}}
```

`$pull` remove a specific item(s) in array

Pulling one:

```
    {
        "$pull" : {
            "todo" : "laundry"
        }
    }
```

Pulling many:

```
    {
        "$pull" : {
            "todo" : [
                 "dishes",
                 "dry cleaning"
            ]
        }
    }
```

##### Positional array modifications

Increment `votes` of the `comments[0]` by 1.

```
    {"$inc" : {"comments.0.votes" : 1}}
```

Find John in `comments.author` and change it to Jim.

```
    db.blog.update(
        {
            "comments.author" : "John"
        },  
        {
            "$set" : {
                "comments.$.author" : "Jim"
            }
        }
    )
```

This only change the first match.

##### Modifier speed
Typically, documents are stored next to each other, so if your documents get 
bigger, they will be moving to the end. Moving is slow
Beware of "paddingFactor" in MongoDB. If you change the size of a document,  
it will leave a hole in memory which will lead to memory inefficiency.

MongoDB is currently not great at reusing free spaces left by moving.
 
TODO: Compacting data and schema design solutions


# Upsert

If no document is found that matches the update criteria, a new document will
 be created by combining the criteria and updated documents.
 
Use "$setOnInsert` to seed document when it is created and not will not updated.

```
    db.users.update(
        {},
        {
            "$setOnInsert" : {
                "createdAt" : new Date()
            }
        },
        true)
```

# Write Concern

Write concern is a client setting used to describe how safely a write should 
be stored before the application continues. By default, inserts, removes, and
 updates wait for a database response—did the write succeed or not?—before continuing.
 

# Queries

### Conditional queries

"$lt", "$lte", "$gt", "$ne", "$gte", "$mod", "$not"

### OR queries

OR condition for a single key: `$in` or `$nin` (not in)

```
    db.users.find(
        {
            "user_id" : {
                "$in" : [12345, "joe"]
            }
        })
```

OR condition with '$or'

```
    db.raffle.find(
        {
            "$or" : [{"ticket_no" : 725}, {"winner" : true}]
        })
        
    db.raffle.find(
        {
            "$or" : [
                {
                    "ticket_no" : {"$in" : [725, 542, 390]}
                },{
                    "winner" : true
                }]
        })
```

### Regular Expressions

Mongo uses  Perl Compatible Regular Expression to match regex. Should check 
with js shell before using in queries.

Find case-insensitive 

```
    db.users.find({"name" : /joe/i})
    return joe and Joe
    
    db.users.find({"name" : /joey?/i})
    return joe and Joe and joey and Joey
```

### Querying Arrays

Query an item in array

```
    db.food.find(
        {
            "fruit" : "banana"
        })
```

Query many items in array

```
    db.food.find(
        {
            fruit : {
                $all : ["apple", "banana"]
            }
        })
```

Query exact match

```
    db.food.find(
        {
            "fruit" : ["apple", "banana", "peach"]
        })
```

Query with specific item value. `fruit[2]` == "peach"

```
    db.food.find(
        {
            "fruit.2" : "peach"
        })
```

### Array and range query interactions

For example, we have:

```
    {"x" : 5}
    {"x" : 15}
    {"x" : 25}
    {"x" : [5, 25]}
```

##### Query with $lt and $gt

Query

```
    db.test.find(
        {
            "x" : {
                "$gt" : 10, "$lt" : 20
            }
        })
```

Return

```
    {"x" : 15}
    {"x" : [5, 25]}
```

Becasue 5 < 20 and 25 > 10.

##### Query with "$elemMatch"

Query

```
    db.test.find(
        {
            "x" : {
                "$elemMatch" : {
                    "$gt" : 10, "$lt" : 20
                }
            }
        })
```

Return

```
    no results
```

Because `$elemMatch` won’t match non-array elements.

##### Query with min() and max()

Query

```
    db.test.find(
        {
            "x" : {
                "$gt" : 10, "$lt" : 20
            }
        }).min({"x" : 10}).max({"x" : 20})
```

Return

```
    {"x" : 15}
```

### Querying on Embedded Documents

##### Querying for the whole document

The following is order sensitive

```
    db.people.find(
        {
            "name" : {
                "first" : "Joe", "last" : "Schmoe"
            }
        })
```

##### Querying for its individual key/value pairs

```
    db.people.find(
        {
            "name.first" : "Joe", 
            "name.last" : "Schmoe"
        })
```

##### Querying in nested embedded documents

Example: want to find comments by Joe that were scored at least a 5

```
{
    "content" : "...",
    "comments" : [
        {
            "author" : "joe",
            "score" : 3,
            "comment" : "nice post"
        },
        {
            "author" : "mary",
            "score" : 6,
            "comment" : "terrible post"
        }
    ]
}
```

These queries won't work
```
    // Match exact document
    db.blog.find(
        {
            "comments" : {
                "author" : "joe",
                "score" : {
                    "$gte" : 5}
                }
            }
        })
        
    // Return the both ??? why both ???
    db.blog.find(
        {
            "comments.author" : "joe",
            "comments.score" : {
                "$gte" :5
            }
        })
```


```
    db.blog.find(
        {
            "comments" : {
                "$elemMatch" : {
                    "author" : "joe",
                    "score" : {
                        "$gte" : 5
                    }
                }
            }
        })
```

# $where Queries

Use aggregation instead

# Server-Side Scripting

```js
    func = "function() { print('Hello, "+name+"!'); }"
```

Might turn to 

```js
    func = "function() { print('Hello, '); db.dropDatabase(); print('!'); }"
```

Which will run `db.dropDatabase()` and you lose entire database.
To prevent this, use scope to pass in a name.

```python
    func = pymongo.code.Code(
        "function() {
            print('Hello, '+username+'!'); 
        }",{
            "username": name
        })
```

# Comparison order

1. Minimum value
2. null
3. Numbers (integers, longs, doubles)
4. Strings
5. Object/document
6. Array
7. Binary data
8. Object ID
9. Boolean
10. Date
11. Timestamp
12. Regular expression
13. Maximum value

# Avoiding Large Skips

Skip is slow and should be avoided

This is a bad implementation. Never do it.

```
    var page1 = db.foo.find(criteria).limit(100)
    var page2 = db.foo.find(criteria).skip(100).limit(100)
    var page3 = db.foo.find(criteria).skip(200).limit(100)
```

Using conditional query instead. For example.

```
    var page1 = db.foo.find().sort({"date" : -1}).limit(100)
    var latest = page1[100]
    
    // Query the next 100 items by querying based on date 
    var page2 = db.foo.find({"date" : {"$gt" : latest.date}}).sort({"date" : -1}).limit(100)
```

# Getting Consistent Results

It is very important to know that if you update your documents, chances are 
they will get bigger and no longer fit to the space they were before. MongoDB
 will move those documents to the end of the collection, so that in some 
 cases for program will run into a loop in which it tries to update the 
 updated objects.

You might want to use 

```
    db.foo.find().snapshot()
```

for updating objects once. Snapshotting makes queries slower.

Inconsistencies arise only when the collection changes under a cursor while 
it is waiting to get another batch of results.

# Chap 5: Indexing

## Introduction

Index dramatically reduces query time by minimizing scanned objects. Indexing comes with a price. It will slows down INSERT, UPDATE, DELETE operations because mongo needs to update index afterward. Should only use a couple of indexes in a collection althought mongoDB support up to 64.

### Create an index

```
	db.users.ensureIndex({"username" : 1})
```

### Create compound indexes

```
	db.users.ensureIndex({"age" : 1, "username" : 1})
```

What it does is that it will sort the collection based on `age` first and then `username`.

Example without indexes

```
	{
		{ "username" : "user0", "age" : 69 },
		{ "username" : "user1", "age" : 50 },
		{ "username" : "user2", "age" : 88 },
		{ "username" : "user3", "age" : 52 },
		{ "username" : "user4", "age" : 74 },
		{ "username" : "user5", "age" : 104 },
		{ "username" : "user6", "age" : 59 },
		{ "username" : "user7", "age" : 102 },
		{ "username" : "user8", "age" : 94 },
		{ "username" : "user9", "age" : 7 },
		{ "username" : "user10", "age" : 80 }
	}
```

With compound index `{"age" : 1, "username" : 1}`

```
	[0, "user100309"] -> 0x0c965148
	[0, "user100334"] -> 0xf51f818e
	[0, "user100479"] -> 0x00fd7934
	...
	[0, "user99985" ] -> 0xd246648f
	[1, "user100156"] -> 0xf78d5bdd
	[1, "user100187"] -> 0x68ab28bd
	[1, "user100192"] -> 0x5c7fb621
	...
	[1, "user999920"] -> 0x67ded4b7
	[2, "user100141"] -> 0x3996dd46
	[2, "user100149"] -> 0xfce68412
	[2, "user100223"] -> 0x91106e23
```

Sorted by `age` and then `username` and each has a pointer to memory location.

### Three most common ways to query with index

##### Point query

Very efficient because it can jump directly to the correct age and return already sorted list.

```
	db.users.find(
		{
			"age" : 21
		}
	).sort(
		{
			"username" : -1
		}
	)
```

##### Multi-value query

Still efficient.

```
	db.users.find({
		"age" : {
			"$gte" : 21, "$lte" : 30
		}
	})
```

##### Multi-value query with sort

Less efficient than the previous one because returning result is not in sorted order. `sort()` depends on how big the result is.

```
	db.users.find({
		"age" : {
			"$gte" : 21,
			"$lte" : 30
		}
	}).sort({
		"username" :1
	})
```

##### Index in reverse order

```
	{"username" : 1, "age" : 1}
```

### Compound Indexes

This matters if you oftern apply sorting on mutiple keys.
For example index:

```
	{"age" : 1, "username" : 1}
```

These sorts are good

```
	{"age" : 1, "username" : 1}
	{"age" : 1, "username" : -1}
	{"age" : -1, "username" : -1}
	{"age" : -1, "username" : 1}
```

But these will take longer

```
	{"username" : 1, "age" : 1}
	{"username" : 1, "age" : -1}
	{"username" : -1, "age" : -1}
	{"username" : -1, "age" : 1}
```

### Covered Indexes
When an index contains all the values requested by the user, it is considered to be covering a query. This type of query is faster because it does not need to follow the pointer to fetch the whole document.

### How $-Operators Use Indexes

##### Inefficient operators

`$where`, `$exists`, `$ne`

##### Ranges

When designing an index with multiple fields, put fields that will be used in exact matches first (e.g., "x" : "foo" ) and ranges last (e.g., "y": {"$gt" : 3, "$lt" : 5} ). This allows the query to find an exact value for the first index key and then search within that for a second index range. Using this way, the query can save time by eliminating documents that to be search for range later.

Example query:

```
	{
		"age" : 47, 
        "username" : {
            "$gt" : "user5", 
            "$lt" : "user8"
        }
    }
```

With index `{"age" : 1, "username" : 1}`, it will return users with `age` 47 very quickly and then do search on those returned documents. It is efficient.

With index `{"username" : 1, "age" : 1}`, it searches for `username` between "user5" and "user8" and then pick out the ones with `age` 47. This forces DB to scan more items and searching for range takes more time than searching for exact value so this approach for inefficient.

##### OR queries

As of this writing, MongoDB can only use one index per query. That is, if you create one index on {"x" : 1} and another index on {"y" : 1} and then do a query on {"x" : 123, "y" : 456} , MongoDB will use one of the indexes you created, not use both. This only exception to this rule is "$or" . "$or" can use one index per $or clause, as $or preforms two queries and then merges the results.

But in general, doing 2 seperate queries is much less efficient than doing one because MongoDB has to loop through the results and remove duplicates. So, prefer `$in` to `$or` whenever possible.

##### Indexing Objects and Arrays

Not sure why you want to do this. Not recommended.

##### Index Cardinality

**Cardinality** refers to how many distinct values there are for a field in a collection. 

As a rule of thumb, try to create indexes on high-cardinality keys or at least put high-cardinality keys first in compound indexes (before low-cardinality keys).

### explain() and hint()

`explain()` is a function that describes how the query works. `explain()` must be called last. Two type of explains:

1. For non-indexed queries
2. For indexed queries

##### Indexed queries

Returned keys:

* **cursor**: Indicate index in query.
* **isMultiKey**: If this query used a multikey index.
* **n**: The number of documents returned by the query.
* **nscannedObjects**: The number of times MongoDB had to follow an index pointer to the actual document on disk
* **nscanned**: The number of documents examined.
* **scanAndOrder**: If MongoDB had to sort results in memory.
* **indexOnly**: If MongoDB was able to fulfill this query using only the index entries.
* **nYields**: The number of times this query yielded (paused) to allow a write request to proceed.
* **millis**: Time to execute the query.
* **indexBounds**: Describes how the index was used.

Call `hint()` to force index. If not, MongoDB will automatically choose an index.

##### The Query Optimizer

MongoDB also provides the query optimizer which will choose a subset of possible indexes, run your query with those indexes in parallel. The first plan returns 100 results is the "winner" and MongoDB will cache that index for this query. That index will be reevaluated after a index is created or after every 1000 queries.

##### When Not to Index

Indexes become less and less efficient as you need to get larger percentages of a collection because using an index requires two lookups:

1. Look at the index entry.
2. Following the index’s pointer to the document.

A table scan only requires one: 

1. Looking at the document.


**Caution**: if a query is returning 30% or more of the collection, start looking at whether indexes or table scans are faster. However, this number can vary from 2% to 60%.

You can force it to do a table scan by hinting {"$natural" : 1}

```
    db.entries.find({"created_at" : {"$lt" : hourAgo}}).hint({"$natural" : 1})
```

### Types of Indexes

##### Unique Indexes

Enforce uniqueness.

```
    db.users.ensureIndex({"username" : 1}, {"unique" : true})
```

**Caution**: 

1. If a key does not exist, the index stores its value as null for that document. This means that if you create a unique index and try to insert more than one document that is missing the indexed field, the inserts will fail because you already have a document with a value of null.

2. All fields must be smaller than 1024 bytes to be included in an index. This means that keys longer than 8 KB will not be subject to the unique index constraints: you can insert identical 8 KB strings, for example.

##### Compound unique indexes

You can do that. For example, we have unique index on `{"username" : 1, "age" : 1}`, so the following is legal but a second copy of any of these documents would cause a duplicate key exception.

```
    db.users.insert({"username" : "bob"})
    db.users.insert({"username" : "bob", "age" : 23})
    db.users.insert({"username" : "fred", "age" : 23})
```

##### Dropping duplicates

If you apply unique index on existing collection, you might key a duplicate key exception. You and force this operation by adding `dropDups` which will only keep one of the duplicate items and remove the rest. 

```
    db.people.ensureIndex({"username" : 1}, {"unique" : true, "dropDups" : true})
```

**Caution**: You have no control over which to keep and which to remove so do not use it with important data.

### Sparse Indexes

**Def**

MongoDB **sparse indexes**: indexes that need not include every document as an entry.

Apply unique key name `email` but do not require it.

```
    db.ensureIndex({"email" : 1}, {"unique" : true, "sparse" : true})
```

Sparse indexes do not necessarily have to be unique.

**Caution**: The same query can return different results depending on whether or not it uses the sparse index.

Example collection:

```
    {"_id" : 0 }
    {"_id" : 1, "x" : 1 }
    {"_id" : 2, "x" : 2 }
    {"_id" : 3, "x" : 3 }
```

We use query

```
    db.foo.find({"x" : {"$ne" : 2}})
```

1. With no index:

```
    {"_id" : 0 }
    {"_id" : 1, "x" : 1 }
    {"_id" : 3, "x" : 3 }
```

2. With index db.ensureIndex({"x" : 1}, {"sparse" : true})

```
    {"_id" : 1, "x" : 1 }
    {"_id" : 3, "x" : 3 }
```

Because `{"_id" : 0 }` does not have key `x` so it is not included in the index.

### Index Administration

* All indexes are stored in *system.indexes* collection.
* *system.indexes* is reserved so you cannot modify or remove items directly
* Modify or remove indexes by calling `ensureIndex` or `dropIndexes`.

Get indexes in a collection:

```
    db.collectionName.getIndexes()
```

**Caution**: The "v" field is used internally for index versioning. If you have any indexes that do not have a "v" : 1 field, they are being stored in an older, less efficient format. You can upgrade them by ensuring that you’re running at least MongoDB version 2.0 and dropping and rebuilding the index.

##### Identifying Indexes

**Caution**: By default, when MongoDB build an index, it blocks all reads and writes on a database until the index build has finished.

**Tips**: Use the background option when building an index. This will yield to other operations but still have severe impact. It is much slower.

**TIPS**: If you have the choice, creating indexes on existing documents is slightly faster than creating the index first and then inserting all documents.
