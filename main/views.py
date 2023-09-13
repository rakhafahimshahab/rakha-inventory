from django.shortcuts import render

def show_main(request):
	context = {
		'application_name': "Rakha's Inventory",
		'name': 'Rakha Fahim Shahab',
		'class' : 'PBP KI'
	}

	return render(request, 'main.html', context)