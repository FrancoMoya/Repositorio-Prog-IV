from django.shortcuts import render
from django.http import JsonResponse
import json
from aplicaciones.usuario.models import Customer
from aplicaciones.pedido.models import Pedido
from aplicaciones.producto.models import Producto
from .models import CarritoProducto

def carrito(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        pedido, created = Pedido.objects.get_or_create(customer=customer)
        items = pedido.carritoproducto_set.all()
        # pedido es la foreign key de carritoproducto
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'carrito/carrito.html', context)

def pago(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        pedido, created = Pedido.objects.get_or_create(customer=customer)
        items = pedido.carritoproducto_set.all()
        # pedido es la foreign key de carritoproducto
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'carrito/pago.html', context)




def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('Producto ID:', productId)
    
    customer = request.user.customer
    producto = Producto.objects.get(id_producto=productId)
    pedido, created = Pedido.objects.get_or_create(customer=customer)
    
    carritoProducto, created = CarritoProducto.objects.get_or_create(id_pedido=pedido, id_producto=producto)
    
    if action == 'add':
        carritoProducto.cantidad = (carritoProducto.cantidad + 1)
    elif action == 'remove':
        carritoProducto.cantidad = (carritoProducto.cantidad - 1)
        
    carritoProducto.save()
    
    if carritoProducto.cantidad <= 0:
        carritoProducto.delete()
    
    return JsonResponse('Item was added', safe=False)
