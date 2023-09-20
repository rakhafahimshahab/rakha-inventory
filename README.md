# rakhas-inventory
# Assignment 2
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
<img src="images/flowchart.png">

# Assignment 3
## Questions
### 1.  What is the difference between POST form and GET form in Django?
The primary variance between POST and GET methods in Django lies in their data transmission mechanisms. POST conveys data within the body of the request, providing enhanced security and being apt for operations that modify data. Conversely, GET relays data by appending it to the URL, which, while less secure, is optimal for data retrieval functions. The selection between these methods should be predicated on the data's characteristics and the intended server operation.
### 2.  What are the main differences between XML, JSON, and HTML in the context of data delivery?
From a data delivery perspective, XML is tailored for intricate, hierarchical data constructs and boasts self-descriptive attributes. JSON, being succinct and easily comprehensible, is the prevalent choice for web application data interchange. HTML, however, primarily serves to delineate the architecture and content of web documents. Your selection between these formats should be driven by your unique data presentation and transmission requisites.
### 3. Why is JSON often used in data exchange between modern web applications?
JSON has risen to prominence in contemporary web application data interchange due to its straightforwardness, efficiency, and language-independent attributes. Furthermore, its widespread acceptance and alignment with the imperatives of swift, compatible, and user-friendly web development make it the favored choice.
## Steps
### Step 1. Configure routing from main/ to /
1. Activate VE:
   - Windows:
    ```
    env\Scripts\activate.bat
    ```
  - Mac:
    ```
    source env/bin/activate
    ```
2. open urls.py in rakhas_inventory. change main/ to ''
   ```
    urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
   ]
   ```
### Step 2. Configure routing from main/ to /
1. Create templates folder inside root directory and create file named base.html. paste the following:
    ```
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta
               name="viewport"
               content="width=device-width, initial-scale=1.0"
         />
         {% block meta %}
         {% endblock meta %}
      </head>

      <body>
         {% block content %}
         {% endblock content %}
      </body>
   </html>
    ```
2. Adjust code in settings.py in rakhas_inventory folder
   ```
   ...
   TEMPLATES = [
      {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [BASE_DIR / 'templates'], # add this line
         'APP_DIRS': True,
         ...
      }
   ]
   ...
   ```

3. Change main.html inside templates in main folder
   ```
   {% extends 'base.html' %}
   {% block content %}
      <h1>Rakha's Inventory Page</h1>

      <h5>Application Name:</h5>
      <p>{{ application_name }}</p>

      <h5>Name:</h5>
      <p>{{ name }}</p>

      <h5>Class:</h5>
      <p>{{ class }}</p>
   {% endblock content %}
   ```
### Step 3. Creating data input form Showing product data in html
1. Create a new file inside main folder named forms.py. paste the following:
    ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
      class Meta:
         model = Product
         fields = ["name","category", "amount", "description"]
         </head>

         <body>
            {% block content %}
            {% endblock content %}
         </body>
      </html>
    ```
2. Add imports to views.py in main folder and create new function called create product
   ```
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   from main.forms import ProductForm
   from main.models import Product
   ```
   ```
   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         form.save()
         return HttpResponseRedirect(reverse('main:show_main'))

      context = {'form': form}
      return render(request, "create_product.html", context)
   ```

3. Change show_main function
   ```
   def show_main(request):
      products = Product.objects.all()

      context = {
         'name': 'Rakha Fahim Shahab', # Your name
         'class': 'PBP KI', # Your PBP Class
         'products': products
      }

      return render(request, "main.html", context)
   ```

### Step 4. XML and JSON
1. Add the following functions in views.py
   ```
   def show_xml(request):
		data = Items.objects.all()
		return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


	def show_json(request):
		data = Items.objects.all()
		return HttpResponse(serializers.serialize("json", data), content_type="application/json")


	def show_xml_by_id(request, id):
		data = Items.objects.filter(pk=id)
		return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


	def show_json_by_id(request, id):
		data = Items.objects.filter(pk=id)
		return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   ```
2. Also add the path in urls.py under urlpatterns = []
   ```
   ...
      path('xml/', show_xml, name='show_xml'),
		path('json/', show_json, name='show_json'),
		path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
		path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
   ...

   ```
## Postman
### Screenshots
1. main
<img src ="/images/postman_main.png">
2. xml
<img src ="/images/postman_xml.png">
3. json
<img src ="/images/postman_json.png">
4. xml1
<img src ="/images/postman_xml1.png">
5. json1
<img src ="/images/postman_json1.png">