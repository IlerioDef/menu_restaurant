<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">menu_restaurant</h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project



Projects consists of two pages:
* Menu
* Order

### Built With

* [![Python][Python.com]][Python-url]
* [![Django][djangoproject.com]][Django-url]
* [![Postgres][postgresql.org]][postgresql-url]
* [![Tailwind][tailwindcss.com]][tailwind-url]
* [![Docker][docker.com]][docker-url] 

<!-- GETTING STARTED -->
## Getting Started

To start a project you will need to perform several actions:
* Build and run docker compose container
* Make manual migrations within the container
* Populate the database with data

### Prerequisites

To run this application you wil need the following:
* Docker

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/IlerioDef/menu_restaurant.git
   ```
2. Move into the folder 
   ```sh
   cd ./menu_restaurant
   ```
3. Run `docker compose`
    ```sh
    docker-compose up -d --build
    ```
   you should see something like this after the process ends:
    ```shell
    Creating menu_restaurant_db_1 ... done
    Creating docker_django        ... done
    ```
4. Check that container is run and alive and get its name
5. Run the shell within the Docker container:
    ```shell
    docker exec -it "<container-name-or-id>" sh
    ```
6. Run the Django ```migrate```
    ```shell
    python manage.py migrate
    ```
7. Make a ```superuser``` for the project
    ```shell
   python manage.py createsuperuser – username=admin – email=admin@admin.com
    ```
   that will make a superuser named ```admin``` and will promt you to enter the password
8. The project will be available on
<a href="0.0.0.0:8000">0.0.0.0:8000</a>
   and you should populate the project with data(dishes, dish categories etc.) under admin login at <a href="0.0.0.0:8000/admin">0.0.0.0:8000/admin</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/ileriodef/menu_restaurant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/IlerioDef/menu_restaurant/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[djangoproject.com]: https://img.shields.io/badge/Django-2B8C67?style=for-the-badge&logo=django&logoColor=white
[django-url]: https://www.djangoproject.com/
[Postgresql.org]: https://img.shields.io/badge/Postgresql-0064a5?style=for-the-badge&logo=postgresql&logoColor=white 
[Postgresql-url]: https://www.postgresql.org/
[Python.com]: https://img.shields.io/badge/Python-444?style=for-the-badge&logo=python&logoColor=white 
[Python-url]: https://www.python.org/
[tailwindcss.com]:https://img.shields.io/badge/TailwindCSS-38bdf8?style=for-the-badge&logo=tailwindcss&logoColor=white 
[tailwind-url]:https://tailwindcss.com/
[docker.com]:https://img.shields.io/badge/Docker-086dd7?style=for-the-badge&logo=docker&logoColor=white 
[docker-url]:https://www.docker.com/
