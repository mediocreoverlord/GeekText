# GeekText
An REST API Service to support an online web application bookstore that targets a particular niche in technology. This is a team project made for FIU Software Engineering I (CEN4010) class of Fall 2023. Each developer was tasked to complete a feature for the REST API through the Flask architecture while working in a Scrum based development structure. *UI was not required but expected in future updates!*

## Set Up
  - Recommended Tools: MySQl | Postman
  - In MySQL, use the scripts file located within the project to load our team database.
  - Once you have cloned the repository, create a JSON file within the resources module name "db_config" and format your MySQL connection information. *Note: If the program is having trouble finding yout db_config file you may need to change the path in         code from resources/db_config.json to the full fille path of your config file.*
  - Ensure MySQL connector and Flask packages are added to your program environment.

## Breakdown
  - The REST API's features are assigned as follows:
  - Book Browsing and Sorting: @gvazq052
      - Users will have a simple and enjoyable way to discover new books and Authors and sort results.
  - Book Details: @mediocreoverlord
      - Users can see informative and enticing details about a book
  - Profile Management: @arianaaurribarri
      - Users can create and maintain their profiles rather than enter in their information each time they order
  - Shopping Cart: @inkdmontana
      - Users can manage items in a shopping cart for immediate or future purchase
  - Book Rating and Commenting: @AsianTRU32
      - Users can rate AND comment on books they’ve purchased to help others in their selection
  - Wish List Management: @JesusVa29
      - Users can create and have 3 different wish lists which can have books moved to from the primary list.

## Endpoint Usage
  - Enpoints can be asked via browser through the link available in your IDE's console once the Flask app is running. However, to test endpoints Postman is recommended. Within Postman you can create different HTTP requests to the assigned routes (specified within code).

