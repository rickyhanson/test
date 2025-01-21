# Todo-List
### Video Demo:
https://youtu.be/AO85wumwlII
### Description:
For the last project, I used the base of the problem _birthdays_ from the **lab 9**. I wanted to make a to-do list with usernames. But unfortunately I did not have enough time to implement accounts with password. I made a table with the name _todo_ in the database _todo.db_ to keep the data of all the tasks that the users want to save. For the display, I made another table named _display_ after the program processed the date into duration until the deadline of each task.

The invalid entries are to be rejected by using the _apology_ function from the **pset 10**, and they are not added to the database. We can go back to the last page if we want to add another valid entry.

First we need to login by using a username without a password and for that, I implemented _login.html_ with one **text** field, and one **submit** button. After the username for the login is filled, we will be redirected to the _index.html_ page. There I implemented a datepicker that disabled all **past** dates, the task name and the description of the task. Lastly, I made another **submit** button to add the entry to the database.

After the entry has been added, the code update the _display_ table that will be displayed on the _index.html_ page. When the task is completed, we can click on the **done!!** button to remove it from the database. If other person wants to use it, click the **logout** button to logout. The former user will then be removed from the current session. If the former user wants to add more entries or delete entries, he or she can login with the same username again.


HTML files:
For the HTML files I used the jinja syntax to make it less prone to the error by making a loop for the whole data given from the python. In the _layout.html_ I made the basic layout for all the html files, i.e., the files that are responsible for the user interface. Then I extend the design from the _layout.html_ to prevent repetition in the codes that can be seen as bad programming style and prone to error in case of an update.

The data given to the field from the _index.html_ will be then given to the python file via "Post" method. After the data has been updated, it will refresh the page to show the update from the database to be shown on the lower side of the page. For the logout I don't need to make the logout page since the user will be redirected to the login page, where they can either input the same username or new username.
