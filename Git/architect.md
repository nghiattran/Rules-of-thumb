```
tree .git/
.git/
|-- HEAD
|-- config
|-- description
|-- hooks
|   |-- applypatch-msg.sample
|   |-- commit-msg.sample
|   |-- post-commit.sample
|   |-- post-receive.sample
|   |-- post-update.sample
|   |-- pre-applypatch.sample
|   |-- pre-commit.sample
|   |-- pre-rebase.sample
|   |-- prepare-commit-msg.sample
|   |-- update.sample
|-- info
|   |-- exclude
|-- objects
|   |-- info
|   |-- pack
|-- refs
    |-- heads
    |-- tags
```

The `.git` directory above is, by default, a subdirectory of the root working directory, testgit. It contains a few different types of files and directories:
* Configuration: the .git/config, .git/description and .git/info/exclude files essentially help configure the local repository.
* Hooks: the .git/hooks directory contains scripts that can be run on certain lifecycle events of the repository.
* Staging Area: the .git/index file (which is not yet present in our tree listing above) will provide a staging area for our working directory.
Object Database: the .git/objects directory is the default Git object database, which contains all content or pointers to local content. All objects are immutable once created.
* References: the .git/refs directory is the default location for storing reference pointers for both local and remote branches, tags and heads. A reference is a pointer to an object, usually of type tag or commit. References are managed outside of the Object Database to allow the references to change where they point to as the repository evolves. Special cases of references may point to other references, e.g. HEAD.

Git remote repository that would not have a working directory, you could initialize it using the `git init --bare` command.

Another file of great importance is the Git index: .git/index. It provides the staging area between the local working directory and the local repository.

It is helpful to understand the interactions that take place between these three areas (the repository, index and working areas) during the execution of a few core Git commands:
* `git checkout [branch]`
  This will move the HEAD reference of the local repository to branch reference path (e.g. refs/heads/master), populate the index with this head data and refresh the working directory to represent the tree at that head.
* `git add [files]`
  This will cross reference the checksums of the files specified with the corresponding entries in the Git index to see if the index for staged files needs updating with the working directory's version. Nothing changes in the Git directory (or repository).

![](object-hierarchy.png)

## The Object Database

The primitive object types are:
* Tree: an element in a tree can be another tree or a blob, when representing a content directory.
* Blob: a blob represents a file stored in the repository.
Commit: a commit points to a tree representing the top-level directory for that commit as well as parent commits and standard attributes.
* Tag: a tag has a name and points to a commit at the point in the repository history that the tag represents.

All object primitives are referenced by a SHA, a 40-digit object identity, which has the following properties:
* If two objects are identical they will have the same SHA.
* If two objects are different they will have different SHAs.
* If an object was only copied partially or another form of data corruption occurred, recalculating the SHA of the current object will identify such corruption.

## Storage and Compression Techniques

Disclaimer: infomation in this file is taken directly from http://aosabook.org/en/git.html
