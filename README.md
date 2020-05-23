#The Book Club

The remit of the assignment was to develop a website that allowed a user to manage a common dataset about a particular domain. In addition, the website needed to exhibit CRUD functionality. Allow the user to create dataset entries, read stored dataset entries, update / edit current dataset entries, and delete entries from a dataset. With this in mind, I decided to develop a website for book reading enthusiasts.

The Book Club is a way for users to track their reading. Users can gain access to a centralised library whereby they can browse for books from a central database. If they find a book in the central library they have read, or want to read, they can add this book to their individual library. In their individual library they can mark these books as 'Read' or 'Want to read'. Users will also have the ability to add books to the central library should they not be able to find a particular book they are looking for. And, should they find a book with details missing, or incorrect details, users have the ability to update that book's record. Finally, users have the ability to delete books from their individual library if they no longer want it to remain part of their individual record.

The Book Club website provides users with the opportunity to gain greater insights into their reading habits and bookmark various titles for future reading, ensuring they are reminded of what they want to read. With further development, via a registration process and log-in system, users will be able to search for specific authors, within particular genres, rate books, leave comments and search for books that are rated highly by the central community. Ultimately, the website will play the role of a community for book lovers to share their experiences and recommendations.

##UX 

I wanted to create a simple, uncluttered, and classic environment for the user. I wanted the website to appeal to the masses, but particularly to the heavy reader that can contribute to the development of the site as well as the content. I have attempted to remain consistent with the layout of the website so that there is minimal deviation from one library to the next, or from one input screen to the next. In addition, I have tried to minimise the website surplus text, use icons where possible with tooltips to provide detailed descriptions, and allow the website to focus on its aim. To create, read, update, and delete books.

The Whimsical wireframe and conceptual data model can be accessed in the 'wireframe' folder of the GitHub repository (Link below).

In terms of the user experience and the CRUD functionality, the following applies:
- **Create** - Users can access the ability to create a library entry via an icon in the navbar which is fixed and always available. The user can add as little, or as much, critical information about the book as they want, however, there must always be a book title and author name entered for the book to save to the central library. In addition, users are able to create new entries in the own collection by clicking the 'Add to My library' button in the central library next to each title that is displayed.
- **Read** - Users are able to read the content of the central library and user library in 'Library' and 'My library', respectively. The content of which is from two separate database collections.
- **Update** - If details are missing from books, or found to be incorrect, users can update each title by accessing the dropdown information of each title and accessing the 'Update book' function. Updating the information presented with modify the books' information saved in the central library.
- **Delete** - Users only have the ability to delete books from their own library so as to ensure books in the central library remain present for other users to access. This function is available in the dropdown section of each book presented.

##Features

- **Homepage** - I wanted the homepage to present a classical feel, displaying monochrome library images on a slideshow that briefly provides the user with an overview of the site's function. In this way, I felt it would encourage the user to delve further into the site to explore its functionality.
- **Library** - The central library, where all the website's books are stored, provides the user with a book title, author name, and a button presenting the user with the option to add that book to their personal library. Upon clicking on a title, further information is displayed to the user. A picture of the book's cover which, when clicked, takes the user to that book's page on an online book store where the user can purchase the book. Furthermore, finer details of the book are presented to the user as well as a button to edit / update the selected title should any details be omitted or incorrect.
- **Update book** - Having clicked on the 'Update book' button in the dropdown section, the user is presented with a page outlining each data component as well as its current entry (The form accesses the information already stored in the dataset for editing). Once updated and submitted, the user is returned to the central library whereby they will see the updated details of the book they have just edited.
- **Add book** - This page affords the user the opportunity to add a book to the central library that may be new or missing. Each of the 4 key components of the book details are linked to datasets within the database allowing for autocomplete and ensure consistency of input. Should an input not already be stored in the dataset, then the new data point will be added and made available to the next user in the autocomplete options. Again, to ensure consistency of input, a date picker has been added to the publication date option. This feature is also included in the 'Update book' function. URL's for both the book image and purchase page can be added to provide the user with the necessary links to purchase the book from the dropdown aspect within the library. No new book can be added to the library without a title and an author. These two fields are the minimum requirements for submission of a new book.
- **My library** - To ensure consistency, the flow and function of this page is almost identical to that of the central library. However, there are a number of small changes to personalise the page. As the books can only be updated from the central library, that button is no longer available within the dropdown section. Instead, it has been replaced with three other buttons. 'Read', 'Want to read', and 'Delete'. By clicking the 'Read' or 'Want to read' buttons the icon replacing the 'Add to my library' will change displaying a tick for 'Read', or an hourglass for 'Want to read'. The default setting is to have the book added to 'My library' with an hourglass icon placing the emphasis on the user to change that to 'Read'. Furthermore, if the user decides that they no longer want a particular book in their personal library, they have the option to delete it. This will delete the book from 'My library' but the title and all its details will still remain in the central library.
- **About** - This page provides the user with a more detailed overview of the website than the homepage and provides a direct link to the contact page within the text should the user feel the need to contact the site administrator.
- **Contact** - This page provides the user with an opportunity to contact the site administrator. Three fields are required in order for the form to be validated and sent. If a field is missing, the appropriate message is displayed to prompt the user. Upon successful submission of the message, the user is taken to a receipt page whereby they are thanked for their message and advised as to how long they should expect a response.
- **Navbar & footer** - All aspects of both have active links associated with them. As I have chosen to use icons for the majority of options, tooltips have been used to advise the user what each icon is for should they hover over that icon for an extended period of time. Each social media icon links to the social media accounts of the store linked to the sale of the books from the library. At smaller screen sizes the footer is removed and added to a sidenav to maximise screen usage.

###Features Left to Implement
There are a number of features I would still like to implement on the website. These include the following:
1. The addition of a registration and login process so there can be multiple users all developing their own libraries from the central collection.
2. Search features in the central library allowing users to find books written by certain authors, search through titles of books from a particular genre, or search for titles with a high user rating.
3. Mimic the search feature within the 'My library' page with the addition of search for 'Read' and 'Want to read'
4. Provide the user with the ability to categorise their books as they see fit, regardless of genre, author, or title.
5. Give each user the opportunity to rate each title they have read and add a comment for other users to view.
6. Add a link to, or position, the comments and ratings within the dropdown element of each book in both the central library and the user's library.
7. Give the user the choice of purchasing locations and possibly an Amazon style pricing guide to the book's current cost in ascending order.

##Technologies Used

Throughout the development of the webpage, there was continuous testing and evaluation to ascertain whether the website functioned as planned.

The website was developed, as previously indicated, with minimalism in mind whilst drawing on the classical library feel to entice users and provide an ambiance that promoted ease and control.

The 'inspect' tool in Google Chrome was the primary testing apparatus for the website when investigating the functionality and usability of the site at various screen resolutions. Whilst developing all sections of the website I continually reverted back to this tool to ensure the product matched my expectations which then informed me as to whether further modifications were required.

In addition to 'inspect' in Google Chrome, I frequented [W3C's HTML validation](https://validator.w3.org/) service as well as [W3C's CSS validation](https://jigsaw.w3.org/css-validator/) service to ensure my code fulfilled the necessary criteria and remove any errors.

Furthermore, in addition to HTML5 and CSS3, I made use of various other programming languages. These included the following:
- **[Python](https://python.org/)** - This language was used to enable me to manipulate and analyse the data presented on the site.
- **[MongoDB](https://mongoDB.com/cloud/atlas/)** - This database management site was used to store the data collected and manipulated on my website.
- **[JavaScript](https://javascript.com/)** - This language was used to help create interactive elements within the site.
- **[Materialize](https://materializecss.com/)** - The design and templates used were predominantly from this site.
- **[Google fonts](https://fonts.google.com/)** - The typeface used on the website was taken from this site.
- **[jQuery](https://jquery.com/)** - This language was used to ease the process of site and data manipulation.
- **[Flask](https://fullstackpython.com/flask.html/)** - This language was used to make specific links from one page to another and form validation within the site.
- **[Bson](https://bsonspec.org/)** - This allowed for data transfer between Mongo DB and the deployed site.
- **[PyMongo](https://pypi.org/project/pymongo/)** - This allows for the python code to interact with the Mongo database.

###Testing
1. **Navbar & footer** 
- All available links were hovered over to ensure a description of the icon was provided.
- Each link was clicked to ensure they took the user to the specified page on the site.
- Repeated all of the above at various screen sizes.

2. **Homepage**
- Ensured there was enough contrast between the text and the background images.
- Made sure the background images rotated at an appropriate speed to allow the user to read the content fully.

3. **Library**
- Clicked on the 'Add to My library' button to ensure the title was added to the user’s library as well as take the user to their library to confirm.
- Accessed to books information by clicking on the title and made sure they were aesthetically pleasing at all screen sizes.
- Clicked on each book cover to confirm it took the user through to that book's page at [Waterstones](https://www.waterstones.com) so the user could purchase it. And, that this page was loaded on a separate tab.
- Clicked the 'Update book' button to ensure the update book page loaded and the relevant information was retrieved from MongoDB for editing.

4. **Update book**
- Altered the details of each component of the book and submitted making sure that after submission the user is taken back to the library and all the updated information is contained within that book's container.
- Typed in each of the key data entry points to ensure the autocomplete function still suggested inputs and was styled correctly.

5. **Add book**
- Tried to submit a book with no input to make sure it wouldn't allow it.
- Tried to submit a book with only the author's name included to make sure it wouldn't allow it.
- Tried to submit a book with only the book's title included to make sure it wouldn't allow it.
- Make sure the correct warnings were visible if these parameters were not met.
- Typed in each of the data requirements to make sure the autocomplete options were made available to the user as well as the date picker with the correct number of years available to the user to pick from.
- Typed in new data in each of the options, submitted the book, and checked to see if those new data points became available to the user in the autocomplete next time they tried to add a book.
- Submitted a successful entry and made sure the button returned the user to the main library to view their entry.

6. **My library**
- After adding a book to 'My library' from the main library, checked to make sure the default icon was the hourglass (Want to read) encouraging the user to either read the book, or actively change the icon.
- Again, checked the functionality of the page and that it mimicked the central library usability. i.e. That the book details were revealed upon clicking on the title and that having clicked on the book cover the user is taken to a page whereby they can purchase it.
- Check that the 'Read' button changes the icon from an hourglass to a tick and also that the 'Want to read' button reverts the icon back to default.
- Clicked on the 'Delete' button to delete the book from the user library and make sure that the user remains in their own library. In addition, also checked that the title deleted from the user library remained in the central library, unaffected.
- Checked the usability and design of these elements at all screen sizes.

7. **About**
- Ensured the page rendered as necessary and the message link in the text took the user to the contact page.

8. **Contact**
- Tried to submit a message with no input to make sure it wouldn't allow it.
- Tried to submit a message with only the users name to make sure it wouldn't allow it.
- Tried to submit a book with a wrong email address to make sure it wouldn't allow it.
- Tried submitting the message with correct user name and email address, but no enquiry, to make sure it would not allow it.
- Make sure the correct warnings were visible if each of these parameters were not met by the user.
- Upon completing the enquiry form correctly, ensure that the 'Submit' button took the user to the receipt page and acknowledged their message.

Whilst working on the project I ran into a number of bugs that I feel have been resolved to my satisfaction. These bugs included:

1. Ensuring the details of the book rendered vertically centred in the dropdown section whilst closing the gap to the book image at smaller screen sizes.
2. Making the homepage slider go full screen was initially problematic.
3. Making sure the contact page presented the warnings to the user following incorrect or missing details instead of just sending the user through to the receipt page.
4. Adding a book to a user library from the central library under a new ID was troublesome.

All of the bugs addressed above have been resolved to my satisfaction.

## Deployment

The site was deployed via Heroku using GitHub, and utilises a single branch. Throughout the development process, at each key phase, I committed the updated files to GitHub so as to back up my work and also allow me to refer back to previous versions of my work. As I had linked my GitHub account to my Heroku account, these pushes were automatically pushed to my Heroku account and updated there, too.

The deployed site, when accessed directly from an iPad or iPhone, largely displays exactly as it did whilst using the inspect feature of Chrome. However, there are a number of buttons at smaller screen sizes where the icon has not reduced in size to match the size of the button. In addition, the warning messages where fields have been incorrectly filled or left blank do not render appropriately on smaller screens sizes. Finally, when clicking on a book in either library to expand the detail associated with that title, the background image seems to expand whereas I hope it would have remained fixed. These are problematic and need addressing in future development of the website.

Deployed site URL: https://https://assignment-three-ben.herokuapp.com/home
GitHub repository URL: https://github.com/benm4ckenzie/assignment-three

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

