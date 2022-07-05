from functions import *
from InvoiceRestaurant_ import InvoiceRestaurant

def is_vip_client(id, clients):
    client_found = True
    is_vip = False
    vip_client = None
    for client in clients:
        if client.id == id and client.type_ticket == 'VIP':
            is_vip = True
            vip_client = client
            break
        elif client.id == id:
            client_found = False
    return is_vip, client_found, vip_client

def register_client_restaurant(clients, products, invoices_rest):
    id = comprobar_num('Ingrese la cedula del cliente: ')
    is_vip, client_found, vip_client = is_vip_client(id, clients)
    if is_vip and client_found:
        for product in products:
            print(f'ID: {products.index(product) + 1}')
            product.print_product()
        
        id_selected_product = comprobar_opcion('Ingrese el ID del producto que desea adquirir: ', len(products))
        quantity = products[id_selected_product]
        
        while quantity == 0:
            id_selected_product = comprobar_opcion('El producto que selecciono ya no se encuentra disponible. Ingrese el ID de otro producto que desea adquirir: ', len(products))
            
        products[id_selected_product].quantity -= 1
        vip_client.foods.append(products[id_selected_product])

        cost = calculate_cost_rest(vip_client.foods)
        discount = calculate_discount(id)
        total = calculate_total(cost, discount)
        print(f'Total: {total}')
        decision = comprobar_opcion('''Desea realizar su compra?
        1. Si
        2. No
        -> ''', 2)

        if decision == 1:
            new_invoice_rest = generate_invoice(id, vip_client)
            new_invoice_rest.print_invoice_rest()
            invoices_rest.append(new_invoice_rest)
            print('Pago realizado con exito')
            vip_client.foods = new_invoice_rest
            return vip_client, invoices_rest
        else:
            return -1, invoices_rest
        
    else:
        return -2, invoices_rest



def generate_invoice(id, vip_client):
    cost = calculate_cost_rest(vip_client.foods)
    discount = calculate_discount(id)
    total = calculate_total(cost, discount)
    new_invoice_rest = InvoiceRestaurant(id, vip_client.foods, cost, discount, total)
    return new_invoice_rest

def calculate_cost_rest(order):
    cost = 0
    for product in order:
        order += product.price
    return cost

def calculate_discount(id):
    perfect_id = is_id_perfect(id)
    discount = 0
    if perfect_id == True:
        discount += 0.15
    return discount

def is_id_perfect(id):
    perfect_id = False
    sum_divisors = 0
    for i in range(1, id + 1):
        if id % i == 0:
            sum_divisors += i
    if id == sum_divisors:
        perfect_id = True
    return perfect_id

def calculate_total(cost, discount):
    return cost - discount