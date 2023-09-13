# rakhas-inventory
## Link
[Click here](https://rakhasinventory.adaptable.app/main/) to access app

## Steps
### Step 1. Create new Django project
1. Create virtual environtment in your new directory:
   ```
   python -m venv env
   ```
2. Activate VE:
   - Windows:
    ```
    env\Scripts\activate.bat
    ```
  - Mac:
    ```
    source env/bin/activate
    ```
3. Create 'requirements.txt' to install dependencies
   ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
   ```
4. Run command :
   ```
     pip install -r requirements.txt
     django-admin startproject shopping_list .
   ```
### Step 2. Creating main application
1. create new application
   ```
     python manage.py startapp main
   ```
2. Register main application into the project.
   Open the settings.py in the project directory, add 'main' to INSTALLED_APPS
   ```
     INSTALLED_APPS = [
    ...,
    'main',
    ...
    ]
   ```
3. Create basic html file in new directory called templates inside the main application
   ```
   <h1>Rakha's Inventory Page</h1>

    <h5>Application Name:</h5>
    <p>{{ application_name }}</p>
    
    <h5>Name:</h5>
    <p>{{ name }}</p>
    
    <h5>Class:</h5>
    <p>{{ class }}</p>
   ```
4. Open models.py and change it to make new variable
   ```
    from django.db import models
    
    class Product(models.Model):
        name = models.CharField(max_length=255)
        category = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()
   ```
5. Creating and applying model migrations
   ```
     python manage.py makemigrations
     python manage.py migrate
   ```
### Step 3. Connecting views to templates
1. Open views.py in the main application, add show_main function
   ```
      from django.shortcuts import render

        def show_main(request):
        	context = {
        		'application_name': "Rakha's Inventory",
        		'name': 'Rakha Fahim Shahab',
        		'class' : 'PBP KI'
        	}
	        return render(request, 'main.html', context)
   ```
### Step 4. URL routing
1. Create urls.py inside the main application directory
   add the following code :
   ```
     from django.urls import path
     from main.views import show_main
      
     app_name = 'main'
      
     urlpatterns = [
          path('', show_main, name='show_main'),
      ]
   ```
2. Edit the urls.py on the django project directory
   ```
     ...
     from django.urls import path, include
     ...
     urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
      ]
   ```
## Flow Chart
<img src="/flowchart.png">