#The Book Club

The remit of the assignment was to develop a website that allowed a user to manage a common dataset about a particular domain. In addition, the website needed to exhibit CRUD functionality. Allow the user to create dataset entries, read stored dataset entries, update / edit current dataset entries, and delete entries from a dataset. With this in mind, I decided to develop a website for book reading enthusiasts.

The Book Club is a way for users to track their reading. Users can gain access to a centralised library whereby they can browse for books from a central database. If they find a book in the central library they have read, or want to read, they can add this book to their individual library. In their individual library they can mark these books as 'Read' or 'Want to read'. Users will also have the ability to add books to the central library should they not be able to find a particular book they are looking for. And, should they find a book with details missing, or incorrect details, users have the ability to update that book's record. Finally, users have the ability to delete books from their individual library if they not longer want it to remain part of their individual record.

The Book Club website provides users with the opportunity to gain greater insights into their reading habits and bookmark various titles for future reading, ensuring they are reminded of what they want to read. With further development, via a registration process and log-in system, users will be able to search for specific authors, within particular genres, rate books, leave comments and search for books that are rated highly by the central community. Ultimately, the website will play the role of a community for book lovers to share their experiences and recommendations.


##UX 

I wanted to create a simple, uncluttered, and classic environment for the user. I wanted the website to appeal to the masses, but particularly to the heavy reader that can contribute to the development of the site as well as the content. I have attempted to remain consistent with the layout of the website so that there is minimal deviation from one library to the next, or from one input screen to the next. In addition, I have tried to minimise the website surplus text, use icons where possible with tooltips to provide detailed descriptions, and allow the website to focus on its aim. To create, read, update, and delete books.

The Whimsical wireframe and conceptual data model can be accessed in the 'wireframe' folder of the GitHub repository (Link below).

In terms of the user experience and the CRUD functionality, the following applies:
- **Create** - Users can access the ability to create a library entry via an icon in the navbar which is fixed and always available. The user can add as little, or as much, critical information about the book as they want, however, there must always be a book title and author name entered for the book to save to the central library. In addition, users are able to create new entries in the own collection by clicking the 'Add to My library' button in the central library next to each title that is displayed.
- **Read** - Users are able to read the content of the central library and user library in 'Library' and 'My library', respectively. The content of which is from two seperate database collections.
- **Update** - If details are missing from books, or found to be incorrect, users can update each title by accessing the dropdown information of each title and accessing the 'Update book' function. Updating the information presented with modify the books' information saved in the central library.
- **Delete** - Users only have the ability to delete books from their own library so as to ensure books in the central library remain present for other users to access. This function is available in the dropdown section of each book presented.


##Features

- **Homepage** - I wanted the homepage to present a classical feel, displaying monochrome library images on a slideshow that briefly provides the user with an overview of the site's function. In this way, I felt it would encourage the user to delve further into the site to explore it's functionality.
- **Library** - The central library, where all the website's books are stored, provides the user with a book title, author name, and a button presenting the user with the option to add that book to their personal library. Upon clicking on a title, further information is displayed to the user. A picture of the book's cover which, when clicked, takes the user to that book's page on an online book store where the user can purchase the book. Furthermore, finer details of the book are presented to the user as well as a button to edit / update the selected title should any details be omitted or incorrect.
- **Update book** - Having clicked on the 'Update book' button in the dropdown section, the user is presented with a page outlining each data component as well as it's current entry (The form accesses the information already stored in the dataset for editting). Once updated and submitted, the user is returned to the central library whereby they will see the updated details of the book they have just editted.
- **Add book** - This page affords the user the opportunity to add a book to the central library that may be new or missing. Each of the 4 key components of the book details are linked to datasets within the database allowing for autocomplete and ensure consistency of input. Should an input not already be stored in the dataset, then the new datapoint will be added and made available to the next user in the autocomplete options. Again, to ensure consistency of input, a date picker has been added to the publication date option. This feature is also included in the 'Update book' function. URL's for both the book image and purchase page can be added to provide the user with the neccessary links to purchase the book from the dropdown aspect within the library. No new book can be added to the library without a title and an author. These two fields are the minimum requirements for submission of a new book.
- **My library** - To ensure consistency, the flow and function of this page is almost identical to that of the central library. However, there are a number of small changes to personalise the page. As the books can only be updated from the central library, that button is no longer available within the dropdown section. Instead, it has been replaced with three other buttons. 'Read', 'Want to read', and 'Delete'. By clicking the 'Read' or 'Want to read' buttons the icon replacing the 'Add to my library' will change displaying a tick for 'Read', or an hourglass for 'Want to read'. The default setting is to have the book added to 'My library' with an hourglass icon placing the emphasis on the user to change that to 'Read'. Furthermore, if the user decides that they no longer want a particular book in their personal library, they have the option to delete it. This will delete the book from 'My library' but the title and all it's details will still remain in the central library.
- **About** - This page provides the user with a more detailed overview of the website than the homepage and provides a direct link to the contact page within the text should the user feel the need to contact the site administrator.
- **Contact** - This page provides the user with an opportunity to contact the site administrator. Three fields are required in order for the form to be validated and sent. If a field is missing, the appropriate message is displayed to prompt the user. Upon successful submission of the message, the user is taken to a receipt page whereby they are thanked for their message and advised as to how long they should expect a response.
- **Navbar & footer** - All aspects of both have active links associated with them. As I have chosen to use icons for the majority of options, tooltips have been used to advise the user what each icon is for should they hover over that icon for an extended period of time. Each social media icon links to the social media accounts of the store linked to the sale of the books from the library. At smaller screen sizes the footer is removed and added to a sidenav to maximise screen usage.

###Features Left To Implement

There are a number of features I would still like to implement on the website. These include the following:
1. The addition of a registration and login process so there can be multiple users all developing their own libraries from the central collection.
2. Search features in the central library allowing users to find books written by certain authors, search through titles of books from a particular genre, or serach for titles with a high user rating.
3. Mimic the search feature within the 'My library' page with the addition of search for 'Read' and 'Want to read'
4. Provide the user with the ability to categorise their books as they see fit, regardless of genre, author, or title.
5. Give each user the opportunity to rate each title they have read and add a comment for other users to view.
6. Add a link to, or position, the comments and ratings within the dropdown element of each book in both the central library and the user's library.
7. Give the user the choice of purchasing locations and possibly an Amazon style pricing guide to the book's current cost in ascending order.


##Technologies Used


In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

##Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.


##Credits

###Content
The details for each book were taken from their respective pages on the [Waterstones](https://www.waterstones.com) website.

###Media
The photos used in this site were obtained from the websites as follows:
library_image_1 - https://i.insider.com/579bb64add0895ce188b49df?width=1190
library_image_2 - https://www.thisiscolossal.com/wp-content/uploads/2017/06/library-1.jpg
library_image_6 - https://www.pixelstalk.net/free-download-library-wallpapers/
library_image_7 - https://www.pixelstalk.net/free-download-library-wallpapers/
library_image_9 - https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Duke_Humfrey%27s_Library_Interior_6%2C_Bodleian_Library%2C_Oxford%2C_UK_-_Diliff.jpg/1200px-Duke_Humfrey%27s_Library_Interior_6%2C_Bodleian_Library%2C_Oxford%2C_UK_-_Diliff.jpg
All book cover images - https://www.waterstones.com


##Acknowledgements
I received inspiration for this project from The Code Institute.