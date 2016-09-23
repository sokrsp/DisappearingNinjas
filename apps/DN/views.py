from django.shortcuts import render

def index(request):
	return render(request, 'DN/index.html')

def ninja(request, color):
	turtles = {
		'orange': 'DN/images/michelangelo.jpg',
		'red': 'DN/images/raphael.jpg',
		'blue': 'DN/images/leonardo.jpg',
		'purple': 'DN/images/donatello.jpg'
	}
	if color in turtles:
		context = {
			'image': turtles[color]
		}
	else:
		context = {
			'image':'DN/images/meganfox.jpg'
		}
	return render(request, 'DN/ninja.html', context)
	
def ninjas(request):
	
	return render(request, 'DN/ninjas.html')