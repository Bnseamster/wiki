# wiki
This project contains a wikipedia style app made with django and includes many different features. This includes supporting the use of the markup language Markdown

### Features
-**Entry Page:** Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, will render a page that displays the contents of that encyclopedia entry.
If an entry is requested that does not exist, the user will be presented with an error page indicating that their requested page was not found.
If the entry does exist, the user will be presented with a page that displays the content of the entry.

-**Index Page:** On this page a user can click on any entry name to be taken directly to that entry page.

-**Search:** The user can type a query into the search box in the sidebar to search for an encyclopedia entry.
If the query matches the exact name of an encyclopedia entry, the user will be redirected to that entry’s page.
If the query does not match the name of an encyclopedia entry, the user will instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were Py, then Python should appear in the search results.

-**New Page:** Clicking “Create New Page” in the sidebar will take the user to a page where they can create a new encyclopedia entry.
Users can enter a title for the page and, in a textarea, will be able to enter the Markdown content for the page. Users can also save their new page.
When the page is saved, if an encyclopedia entry already exists with the provided title, the user will be presented with an error message.
Otherwise, the encyclopedia entry will be saved, and the user should be taken to the new entry’s page.

-**Edit Page:** On each entry page, the user is able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
The textarea is pre-populated with the existing Markdown content of the page & the user can click a button to save the changes made to the entry.

-**Random Page:** Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.

-**Markdown to HTML Conversion:** On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user using  
