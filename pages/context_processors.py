from pages.models import Page

def get_pages(request):
    
    pages = Page.objects.order_by( 'order' ).values_list('id', 'title', 'slug')
    #######################################flat=True /////pasa texto plano
    
    return{
        'pages' : pages
    }   