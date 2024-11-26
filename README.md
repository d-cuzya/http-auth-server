# **Http Flask Authentication Server**
___
#### This pet-project uses the python "Flask" framework. Has a connection with Postgresql. The file settings.json has database connection settings and additional flask settings.
##### Database structure:
###### Table "users":
+ id
+ email
+ password
#### The password is not saved in its original form, its hash amount is saved instead (sha256).
#### There are 3 pages "/", "/login" and "/register".
#### There are plans to add:
+ Async
+ Personal profile
+ Session storage cookies
+ The ability to publish posts, view their
+ Access to some publications only by link
+ I am creating my own markdown editor on the site (therefore, the posts will be stored in markdown format)
+ Improve the architecture of the project
+ Improve html, css and js
