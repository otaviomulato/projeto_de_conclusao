from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from dados.models import Produto
from .cart import Cart
from decimal import Decimal
import json
from django.views.decorators.csrf import csrf_exempt

# --- API Endpoints ---

@csrf_exempt
def cart_detail_api(request):
    cart = Cart(request)
    cart_items = []
    for item in cart:
        image_url = None
        if item['product'].dados_img.exists():
            image_url = item['product'].dados_img.first().img_produto.url
            
        cart_items.append({
            'product_id': item['product'].id,
            'name': item['product'].nome_produto,
            'price': str(item['price']),
            'quantity': item['quantity'],
            'total_price': str(item['total_price']),
            'image': image_url,
            'customization': item.get('customization', {})
        })
    
    return JsonResponse({
        'items': cart_items,
        'total_price': cart.get_total_price(),
        'total_items': len(cart)
    })

@csrf_exempt
@require_POST
def cart_add_api(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    
    try:
        data = json.loads(request.body)
        quantity = int(data.get('quantity', 1))
        customization = data.get('customization', {})
    except (ValueError, json.JSONDecodeError):
        quantity = 1
        customization = {}

    cart.add(product=product, quantity=quantity, override_quantity=False, customization=customization)
    
    return JsonResponse({
        'status': 'success',
        'message': 'Produto adicionado ao carrinho',
        'cart_total_items': len(cart)
    })

@csrf_exempt
@require_POST
def cart_update(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Produto, id=product_id)
    
    cart.add(product=product, quantity=quantity, override_quantity=True)

    item_price = Decimal(cart.cart[str(product_id)]['price'])
    item_total = item_price * quantity
    
    return JsonResponse({
        'status': 'ok',
        'cart_total_price': cart.get_total_price(),
        'cart_total_items': len(cart),
        'item_total_price': item_total, 
    })

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail') # Redireciona para evitar erro de JSON se acessado direto

def cart_detail(request):
    cart = Cart(request)
    # ATENÇÃO: O Django vai procurar isso em cart/templates/cart/cart.html
    return render(request, 'cart/cart.html', {'cart': cart})