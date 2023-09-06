# Django
### Aim
To create a wikipedia website where users can read, write and edit arcticles. This project helps in understanding basic Django functionalities including url address, backend server processing and difference between `GET` and `POST` request.  

### Tasks
The main tasks of build wikipedia website can be sub-divided into:
- Enabling users to view wiki pages
- Create wiki page
- Edit wiki page
- Search wiki page

### Learnings
1. **Django Basic:**
Django is a web framework which support backend development of the website. Inside a Django project a user can have multiple apps, for example, Google website is a project, but Google keyword search, Image Search, Shopping, Videos, etc can act as apps. Django helps in building a website design which helps in navigating between apps, while enabling the user maintain good coding practice by not entangling codebase of different apps.

2. **Django Url.py:**
Django `url.py` file helps in determine what url address should lead to which html template as well as what backend function should be used to `GET` that request.

3. **Django view.py:**
Django `url.py` file refer to `view.py` functions which in turn renders the corresponding webpage to your app. You can even have appropriate `GET` and `POST` response defined in the `view.py` file.

4. **HTML Layout Template:**
Using Django, we can define a `html` layout template which can then be refer by other `html` pages thereby reducing redundant effort of copy-pasting the same layout html tags. This also make it easier to make changes to layout in future, since you only need to make change at one place.

5. **Dynamic HTML content:**
Using Django, we can send backend variables to `html` pages, which can further displayed to end-user. Django also enable the developer to have `for loop`, `if conditions` inside the `html` page.
