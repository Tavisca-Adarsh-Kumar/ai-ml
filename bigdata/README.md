# Bigdata

## Hadoop

- An open-source framework for `storing and processing massive datasets`.

### Hadoop Distributed File System (HDFS)

- It carries out the storing, and MapReduce takes care of the processing.

## MapReduce

- A `programming model` that allows you to `process vast amount of data`.

## Spark

- A flexible alternative to MapReduce
- It can use data stored in a variety of formats
    - Cassandra
    - AWS S3
    - HDFS
    - And more
### Spark Resilient Distributed Dataset (RDD)

- Immutable, lazily evaluated, and cacheable
- RDD operation types:
    - Transformations
        - Filter
        - Map
        - FlatMap
    - Actions
        - First
        - Collect
        - Count
        - Take
- Par RDD
    - It will be holding their values in tuples (key, value)
    - It offers better partitioning of data and leads to functionality based on reduction
    - Actions
        - Reduce
        - ReduceByKey

### Features

- Distributed collection of data
- Fault-tolerant
- Parallel operation - partitioned
- Ability to use many data sources

### Spark Ecosystem

- Spark SQL
- Spark DataFrames
- MLlib
- GraphX
- Spark Streaming

## Spark vs MapReduce

Spark   | MapReduce
--      | --
Support many data sources | Required HDFS for storing files
Perform operations upto 100x faster than MapReduce. | 
Keeps most of data in memory after each transformation. It can spill over to disk if memory is filled. | Writes most data to disk after each map and reduce operation.
