# My Copy of the FSND VM
### Log Anaylsis Project

Work can be found in [/vagrant/project](https://github.com/DanPiston/fullstack-nanodegree-vm/tree/master/vagrant/project).

Views created:
1 - Art Paths to connect the articles table to the log table:
```SQL
CREATE VIEW art_path AS
    SELECT title, '/article/' || slug AS path 
    FROM articles;
```

2 - author_path created to associate the authors with their article slugs, which can be used in the full path joining the log table:
```SQL
CREATE VIEW author_path AS
    SELECT authors.name, '/article/' || articles.slug AS path
    FROM authors
    JOIN articles 
    ON authors.id = articles.author;
```
