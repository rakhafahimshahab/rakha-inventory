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

# Assignment 4
## Questions
### 1. What is UserCreationForm in Django?
UserCreationForm is a form provided by Django's built-in authentication framework. It's designed to simplify the creation of new user instances. Its advantages include rapid development due to pre-implemented fields and methods, built-in security measures for password handling, and automatic validation for fields like usernames. However, it has disadvantages such as limited default fields, potentially necessitating extensions for complex registration processes, and possible future challenges if migrating away from Django's built-in authentication.
### 2. What is the difference between authentication and authorization in Django application? Why are both important?
Authentication: This refers to the process of verifying the identity of a user. In a Django application, authentication checks whether a user is who they claim to be, typically through a username and password combination. Django's built-in django.contrib.auth system provides tools for user authentication.

Authorization: Once a user's identity is verified, authorization determines what that user is allowed to do. In Django, this means defining permissions that dictate what actions a user (or a group of users) can perform on specific objects or models. For example, a user might be authorized to view a post but not edit or delete it.

Importance:
Both are crucial for ensuring the security and proper functioning of a Django application. Authentication prevents unauthorized access by ensuring only registered and validated users can log in. Authorization, on the other hand, ensures that once logged in, users can only perform actions they're permitted to, protecting data and functionality from unintended access or modification.
### 3. What are cookies in website? How does Django use cookies to manage user session data?
In Django, cookies play a pivotal role in session management. By default, a cookie stores only a session ID, allowing the server to identify and maintain a user's session across requests by referencing the actual session data kept securely in the database. However, Django can also be configured to store the entire session data directly within the cookie, encrypting it for safety. While this direct storage can be more efficient in some cases, it comes with size constraints and potential security considerations. In essence, Django's use of cookies balances between efficiency and security in managing user sessions.
### 4. Are cookies secure to use? Is there potential risk to be aware of?
Cookies, integral to web technologies, present both utility and potential security vulnerabilities. When transmitted over unencrypted connections, they risk interception, especially if they contain sensitive data. Websites susceptible to Cross-site Scripting (XSS) can inadvertently expose cookies to theft. Reliance solely on cookies without additional safeguards can also open doors to Cross-site Request Forgery (CSRF) attacks. Session hijacking is another concern, where an attacker, after obtaining a user's session cookie, can achieve unauthorized account access.

There are also concerns about third-party cookies, often used by advertisers, which can track users across multiple sites, raising privacy issues. However, several mitigation strategies exist. Enforcing encrypted HTTPS connections, using the HttpOnly flag to prevent JavaScript access, setting the Secure flag to ensure cookies transmit only over HTTPS, and employing the SameSite attribute all enhance cookie security. Moreover, setting short expiration times and consistently sanitizing user inputs further bolster security. In essence, while cookies are invaluable, their careful management is paramount for maintaining both functionality and security.
## Steps
1. add login,logout and register function to views.py
   ```
   from django.shortcuts import render
   import datetime
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   from main.forms import ProductForm
   from main.models import Product
   from django.http import HttpResponse
   from django.core import serializers
   from django.shortcuts import redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages
   from django.contrib.auth import authenticate, login,logout
   from django.contrib.auth.decorators import login_required

   @login_required(login_url='/login')
   def show_main(request):
      products = Product.objects.filter(user=request.user)

      context = {
         'application_name': "Pirates Database",
         'name': request.user.username, # Your name
         'class': 'PBP KI', # Your PBP Class
         'products': products,
         'last_login': request.COOKIES['last_login'],
      }

      return render(request, "main.html", context)

   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         product = form.save(commit=False)
         product.user = request.user
         product.save()
         return HttpResponseRedirect(reverse('main:show_main'))
      context = {'form': form}
      return render(request, "create_product.html", context)

   def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")

   def register(request):
      form = UserCreationForm()

      if request.method == "POST":
         form = UserCreationForm(request.POST)
         if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)

   def login_user(request):
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main")) 
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response
         else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
      context = {}
      return render(request, 'login.html', context)

   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response

   ```
2. create new html file for login page
   ```
   {% extends 'base.html' %}

   {% block meta %}
      <title>Login</title>
   {% endblock meta %}

   {% block content %}

   <div class = "login">

      <h1>Login</h1>

      <form method="POST" action="">
         {% csrf_token %}
         <table>
               <tr>
                  <td>Username: </td>
                  <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
               </tr>
                     
               <tr>
                  <td>Password: </td>
                  <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
               </tr>

               <tr>
                  <td></td>
                  <td><input class="btn login_btn" type="submit" value="Login"></td>
               </tr>
         </table>
      </form>

      {% if messages %}
         <ul>
               {% for message in messages %}
                  <li>{{ message }}</li>
               {% endfor %}
         </ul>
      {% endif %}     
         
      Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

   </div>

   {% endblock content %}

   ```
3. create new html file for register page
   ```
   {% extends 'base.html' %}

   {% block meta %}
      <title>Register</title>
   {% endblock meta %}

   {% block content %}  

   <div class = "login">
      
      <h1>Register</h1>  

         <form method="POST" >  
               {% csrf_token %}  
               <table>  
                  {{ form.as_table }}  
                  <tr>  
                     <td></td>
                     <td><input type="submit" name="submit" value="Daftar"/></td>  
                  </tr>  
               </table>  
         </form>

      {% if messages %}  
         <ul>   
               {% for message in messages %}  
                  <li>{{ message }}</li>  
                  {% endfor %}  
         </ul>   
      {% endif %}

   </div>  

   {% endblock content %}

   ```
4. add logout button in main.html
   ```
   ...
   <br />

   <h5>Last login session: {{ last_login }}</h5>
   ...

   ```
5. add new url to login.html and register.html
   ```
   from django.urls import path
   from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id,register,login_user,logout_user

   app_name = 'main'

   urlpatterns = [
      path('', show_main, name='show_main'),
      path('create-product', create_product, name='create_product'),
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
   ]

   ```
6. change models.py to connect product to user
   ```
   from django.db import models
   from django.contrib.auth.models import User

   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      category = models.CharField(max_length=255)
      amount = models.IntegerField()
      description = models.TextField()

   ```