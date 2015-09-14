# Learning-Hadoop

I started with the Udacity [Introduction to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) online course. I would recommend this course to anyone who is willing to get started with Hadoop; one of the main reasons being the easy-to-setup VM in the course which comes with Cloudera's CDH. 

I found this [video](https://www.youtube.com/watch?v=bcjSe0xCHbE) pretty useful and unique to understand the objectives of the Mappers and Reducers in a Hadoop job. And [this](http://bradhedlund.com/2011/09/10/understanding-hadoop-clusters-and-the-network/) is a pretty comprehensive article that helped me understand the architecure.  

This repository will be updated with the mapreduce codes I will write for the mini projects. My goal in maintaining this repository will be to keep a track of what I have done and also help anyone to get started with Hadoop. 

#### Task 1
Data Set - [Access log](http://content.udacity-data.com/courses/ud617/access_log.gz)
    
    Objective - Compute the number of hits on every file. 
    Mapper Output - Page Name (Key), 1 (value)
    Reducer Ouput - Page Names with the total number of hits

    Example - /assets/js/jquery.form.js 	1803    
    
The other two tasks with the same data set - number of hits by IP and the most popular path - can be completed with some minor changes in mapper code.
    
#### Task 2
Data Set - [Forum data](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz)

    Objective - Create an inverted index
    Mapper Ouput - Word (Key), Node ID (value)
    Reducer Output - Word, Word count, Sorted list of node ids where the word can be found
    
    Example - fantastically 	5 	[17583, 1007765, 1025821, 7004477, 9006895]

##### More to follow.
