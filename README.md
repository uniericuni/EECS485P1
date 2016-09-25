### Group Name: (QHY)

### Group Number: group99

### Members:
  - Eric Hsin (erhsin): create tables, load data into tables
  - Yun-Tzu Chang (ytchang): index, view album list, view album, edit album list, edit album
  - Grace Wu (hygwu): viewing albums and pictures, deploy

### Live Access:
  - http://class6.eecs.umich.edu:6450/24b8g606/p1/

------

# Commands

In the following content, we provied simple commands for you to create, delete tables and load data into the created tables. Noticing that all the tables and content are assigned in `tbl_create.sql` and `load_data.sql`. Plus, `load_data.sql` is generated via `generate_load_data.py`. You have to modify them in order to get customized dataset.

- Create the given set of tables in your database
```
> mysql -u usr_name db_name -p < tbl_create.sql
```

- Remove the given set of tables, including all the table content, from your database
```
> mysql -u usr_name db_name -p < set_default.sql
```

- Load the given set of information into our given tables
```
> mysql -u usr_name db_name -p < load_data.sql
```
