This is an application that presents voting data (mostly). This data is from a legacy database and most of it is limited to delta state in Nigeria.
There are three endpoints that are exposed to the user for interacting with this database:
1. julesbincom.herokuapp.com
This is the root url and it prompts you for the polling unit unique ID of the polling unit you desire the results of.
2. julesbincom.herokuapp.com/1
This endpoint leads you to a page that allows you select a particular local government area (limited to delta state), and after making your choice, you get the total results of ALL the polling units in the selected local government area.
3. julesbincom.herokuapp.com/2
This endpoint leads to a page that allows you store the results of all parties for a new polling unit.
 
