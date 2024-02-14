<a id="readme-top"></a>
<br />

<div align="center">
  <a href="https://guyrimel.github.io/Portfolio-Site/index.html">
    <img src="media/RLogoNoName.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best Recipes Ever</h3>

  <p align="center">
    A simple, intuitive recipe app built with Django and hosted with Heroku. Plugged into a SQL database, works right in the browser. Create and save the best recipes to your heart's content. This application was built as part of CareerFoundary's Web-Developer certificate program.
  </p>
</div>
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#ux-notes">UX Notes</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
<!-- SCREENSHOT -->
<img
  alt="BRE Screenshot"
  src="media/screenshots/screenshot01.png"
  style="height: 16rem; width: auto;"
/>

<!-- KEY FEATURES -->
### Key Features

1. Featuring a simple "Netflix inspired" tile layout
2. Search for recipes by Name or Ingredient
3. View helpful graphs about which recipes need improvement
4. Save your recipes for all time

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUILT WITH -->
### Built With

- HTML, CSS, JavaScript
- Python 3
- Django
- Pandas

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

<!-- PREREQUISITES -->
### Prerequisites
- Python 3
- Please see the "requirements.txt" file

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTALLATION -->
### Installation

Note: Run these commands in the terminal from the desired root directory

1. Clone the repo
   ```sh
   git clone https://github.com/GuyRimel/BRE-Deployment.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Migrate the database
   ```sh
   python manage.py migrate
   ```
3. Run the local server
   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- UX NOTES -->
## UX-Notes

- Login with username: "username" and password: "brepassword" (this is a standard account not currently able to delete recipes)
- Click on a recipe tile to see its details
- Click on the "Records" tab to search recipes by Name or Ingredient (and see helpful charts).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PROJECT DEPLOYMENT -->
## Project Links

Project Deployment: [https://bestrecipesever-3d5fc87c55f3.herokuapp.com/](https://bestrecipesever-3d5fc87c55f3.herokuapp.com/)

Project Repository: [https://github.com/GuyRimel/BRE-Deployment](https://github.com/GuyRimel/BRE-Deployment)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SCREENSHOTS -->
## Screenshots

![sreenshot](media/screenshots/screenshot00.png)

![sreenshot](media/screenshots/screenshot01.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See <a href="LICENSE.txt">`LICENSE.txt`</a> for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
