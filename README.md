# WeBlog_REST_API


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      </li>
	      <ul>
		       <li><a href="#built-with">Built With</a></li>
	     </ul>
	    <li>
	      <a href="#getting-started">Getting Started</a></li>
	      <ul>
	        <li><a href="#installation">Installation</a></li>
	        <li><a href="#prerequisites">Prerequisites</a></li>
</ul>
<li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
 
    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

WeBlog  is a python project created using DjangoRestframework.
An Online blogging Application with  Admin and Users. The authorisation is done using the jwt barer tokenisation .Various features like email ,user profile are included in this project

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[Django]: https://docs.djangoproject.com/en/4.1/
[Django Restframework]: https://www.django-rest-framework.org/
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/cargil-francis/WeBlog_REST_API.git
   ```
2. CD to project
   ```sh
   cd WeBlog_REST_API
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



Follow the given steps to run the project in your localhost. 

### Prerequisites
* Install Python
  ```
  $ sudo apt install python3
  ```
* Create an environment
  ```
  $ python3 -m venv venv
  ```
  
* Activate environment
  ```
  $ source env/bin/activate
  ```

* Install dependencies
  ```
  $ (venv)  python -m pip install -r requirements.txt
  ```

* Make migrations
  ```
  $ (venv)  python3 manage.py makemigrations
  ```

* Migrate models
  ```
  $ (venv)  python3 manage.py migrate
  ```

* Run the project
  ```
  $ (venv)  python3 manage.py runserver
  ```




<!-- USAGE EXAMPLES -->
## Usage

Screenshots of the project using Postman
*User Registeration
 ![Screenshot from 2023-03-23 02-07-20](https://user-images.githubusercontent.com/96044398/227236167-9c44ce41-f2e1-435a-859d-b23cfe91519e.png)
*Login Using 
JWT Token
![Screenshot from 2023-03-23 12-25-38](https://user-images.githubusercontent.com/96044398/227235956-2d3de5bf-830d-433b-9417-74730b63ef24.png)

 
*Create Blog 
![Screenshot from 2023-03-23 13-04-04](https://user-images.githubusercontent.com/96044398/227236510-b3bd7327-62ef-4380-b706-e7580f9a7ccc.png)


*List blog
![Screenshot from 2023-03-23 14-25-36](https://user-images.githubusercontent.com/96044398/227235710-d284ed66-5019-4542-ac46-f85e828b0853.png)

*Update Blog



*Token blacklist
![Screenshot from 2023-03-03 12-14-50](https://user-images.githubusercontent.com/96044398/222651928-4f8658ef-18c2-4c4c-a966-d0846a4bb7bb.png)




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
UserSection
-[X] User Authentication:a.Users will be able to create an account, log in, and log out.

-[X] Newly registered users should receive an email upon registration.

-[X] Blog Posts:a.Users can perform CRUD operations in their own blog posts.

-[X] Users can view the list & details of all blog posts, including blogs posted byother users.

-[X] Users should be able to upload image attachments with the blog.

-[X] A blog post should have a title, content, created time & updated time. The restof the fields should be added as per requirement.

-[X] Users can add comments to any posts.

-[X] A user should be able to see all the comments that are posted under a blogpost.

-[X] Only the author of the comment will be allowed to edit or delete thecomments.

-[X] The created time & updated time of the comment should be saved.

 AdminSection
 
-[X] AdminSection1.Authentication:Admins will be able to log in and log out.

-[X] A new admin user can only be registered by another authenticated adminuser. 

-[X] Blog Posts:Admins can view the list & details of all blog posts.

-[X] Admins should be able to delete blog posts.

-[X] Comments:Admins can view the list of all comments under a post.

-[X] Admins should be able to delete comments.




<p align="right">(<a href="#readme-top">back to top</a>)</p>
