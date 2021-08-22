# PackIOT FSC :: Database

<!-- TOC -->
## 0. Table of contents

- [1. Introduction](#1-introduction)
- [2. Modelling](#2-modelling)
- [3. Implementation](#3-implementation)
- [4. Possible improvements](#4-possible-improvements)
- [5. Where to now?](#5-where-to-now)
    
<!-- /TOC -->
## 1. Introduction

In the context of a hypothetical factory floor, the scope of the challenge is to build a database structure that is capable of storing the number of parts produced, by different machines.

The following are the business domain requirements, associated to the features that this persistence layer must have:

* Each machine has **one** counter to store the production of parts to support reports by period;
* Each machine has **one or more** shifts working per day, starting and ending everyday at the **same time**, on **all days** of the week;
* Counter value is incremental on the source. A new value is added to the table every one minute. So, for each counter, the respective table has the reading on the source for the respective time when it was read, which can be higher than the previous value, or not, if there was no change;
* Counter can be reset back to zero at any time at the source and we do not have control over it;
* Due to the behavior on the pipeline connecting the source to the database, a counter reading might not arrive sorted by timestamp, which means, you can expect to receive readings that are older than the most recent reading for a given counter.
## 2. Modelling

With the specification in hand, we can now go to the entity modelling stage. The result of this is representated below by an entity-relationship diagram (ERD), in a more conceptual form, using [Chen's notation](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model):

![screenshot](../resources/img/erd-1.png)

## 3. Implementation

Before going straight to the implementation aspects, is presented below an alternative version of the previous ERD, with emphasis to the physical structure of the tables that will compose the database:

![screenshot](../resources/img/erd-2.png)

Note that the types of each attribute are in accordance with the SQL type system that the PostgreSQL v11 supports.

## 4. Possible improvements

## 5. Where to now?

* [Root](../README.md)
* [Scripts](../scripts/README.md) 
* [Table of contents](#0-table-of-contents)