from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from core.models import Cocktail
from users.models import CustomUser
from django.db.models import Case, BooleanField, Value, When, Q #For annotation purposes
from operator import attrgetter #For sorting the list with objects
from django.contrib import messages #To communicate that login is required for making it a favorite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # For the paginator

def about(request):
    return render(request, 'core/about.html')

#@login_required
def search(request):
    
    if request.method == 'GET':
        query = request.GET.get('q','')
        user = request.user

        if query:
            result_query = Cocktail.objects.filter(Q(strDrink__icontains=query) | Q(idDrink__icontains=query))

            # Making sure that users that are not logged in can still search
            if not (user.id):
                result_annotated = result_query.annotate(user_fav=Value(False, BooleanField())).order_by('idDrink')#.distinct('strDrink')
            else:
                result_annotated = result_query.annotate(user_fav=Case(
                                When(customuser=user, then=True),
                                default=False,
                                output_field=BooleanField()
                )).order_by('-user_fav','idDrink')#.distinct('strDrink')

            result_final = result_annotated

            total_items = len(result_final)
            items = request.GET.get('all_items', 12) 

            if request.GET.get('all_items'):
                items = total_items
            
            # Makes sure that the standard response is one in case it was just a simple search
            page = 1
            # DISABLED AS WE ARE NOT USING PAGES page = request.GET.get('page', 1)
            
            paginator = Paginator(result_final, items)
            try:
                result_final_page = paginator.page(page)
            except PageNotAnInteger:
                result_final_page = paginator.page(1)
            except EmptyPage:
                result_final_page = paginator.page(paginator.num_pages)

            # Will be displayed when the query returned none
            error_msg = "No cocktails match your search"

            context = {
            'result':result_final_page,
            'error_msg':error_msg,
            'total_items':total_items,
            'items': len(result_final_page),
            'remaining_items': (total_items - items)
            }

        elif not query:
            #Empty query
            highlighted_cocktails = list(Cocktail.objects.filter(idDrink__in=(11003,11001,12127,17206,11007,11005,11004,11009)))
            error_msg = "Type in a keyword to find cocktails"

            print(highlighted_cocktails)

            context = {
            'error_msg':error_msg,
            'result':highlighted_cocktails
            }
        
    #TODO: Build a post request response as it is not used
    return render(request, 'core/search.html', context)

# Used for search
def update_favorites(request):
    if request.method == 'POST':
        
        user = request.user
        drink_id = request.POST.get('drink_id','')
        update_type = request.POST.get('update_type')
        #update_column = request.GET['update_column']
        # print(drink_id)
        # print(update_type)

        if update_type == 'add':
            
            #WORKS: print(user.fav_cocktails.all())
            if user.fav_cocktails.filter(idDrink=drink_id):
                return HttpResponse("Cocktail id: " + drink_id + " - Already favorite")
            else:
                user.fav_cocktails.add(drink_id)
                return HttpResponse("Cocktail added: " + drink_id)

        elif update_type == 'remove':
            
            if not (user.fav_cocktails.filter(idDrink=drink_id)):
                return HttpResponse("Cocktail id: " + drink_id + " - Cannot remove - Not a favorite")
            else:
                user.fav_cocktails.remove(drink_id)
                return HttpResponse("Cocktail removed: " + drink_id)

        return HttpResponse('ERROR: Update type not specified in request')
    
    else:
        return HttpResponse('ERROR: GET request not supported')
