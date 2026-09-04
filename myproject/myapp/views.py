from django.http import HttpResponse
from django.template import context
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello, welcome to my Django app!")

# def view_marks_1(request, marks):
#     if marks >= 40:
#         result = "pass"
#     else:
#         result = "fail"
#     return HttpResponse(f"Your Score: {marks} | Status: {result}")

# def view_marks_2(request, marks):
#     if marks >= 80:
#         result = "excellent"
#     elif marks >= 60:
#         result = "good"
#     elif marks >= 40:
#         result = "average"
#     else:
#         result = "fail"
#     return HttpResponse(f"Your Score: {marks} | Status: {result}")


# def menuitems(request):
#     items = {
#         'pizza': {'name': 'Pizza', 'price': 500},
#         'burger': {'name': 'Burger', 'price': 25},
#         'noodles': {'name': 'Noodles', 'price': 40},
#     }
#     menu_list = ', '.join(
#         f"{data['name']} costs Rs. {data['price']}"
#         for data in items.values()
#     )
#     return HttpResponse(menu_list)

# def menu(request, item):
#     items = {
#     'pizza': {'name': 'Pizza', 'price': 500},
#     'burger': {'name': 'Burger', 'price': 25},
#     'noodles': {'name': 'Noodles', 'price': 40}
# }
#     if item in items:
#         data = items[item]
#         return HttpResponse(f"{data['name']} costs Rs. {data['price']}")
#     else:
#         return HttpResponse("Item not found")

# def recipe(request):
#     food = request.GET.get("food")
#     city = request.GET.get("city")
#     food_type = request.GET.get("type")

#     return HttpResponse(
#         f"food: {food}<br>city: {city}<br>Type: {food_type}"
#     )

# def addition(request):
#     value1 = request.GET.get("value1")
#     value2 = request.GET.get("value2")
#     result=int(value1)+int(value2)
#     try:
#         value1=float(value1)
#         value2=float(value2)
#     except ValueError:
#         return HttpResponse("Invalid input. Please provide numeric values.")
#     return HttpResponse(f"addition of 2 numbers: {result}")

# def calculator(request):
#     value1 = request.GET.get("value1")
#     value2 = request.GET.get("value2")
#     operation = request.GET.get("operation", "add")

#     try:
#         value1 = float(value1)
#         value2 = float(value2)
#     except (TypeError, ValueError):
#         return HttpResponse(
#             "Please provide numeric values using value1 and value2."
#         )

#     if operation == "add":
#         result = value1 + value2
#     elif operation == "subtract":
#         result = value1 - value2
#     elif operation == "multiply":
#         result = value1 * value2
#     elif operation == "divide":
#         if value2 == 0:
#             return HttpResponse("Cannot divide by zero.")
#         result = value1 / value2
#     else:
#         return HttpResponse(
#             "Invalid operation. Use add, subtract, multiply, or divide."
#         )

#     return HttpResponse(f"Result: {result}")


def user_profile(request,username):
    return HttpResponse(
        f'User Profile:{username}'
    )

def item_detail(request, item_id):
    return HttpResponse(
        f'Item ID: {item_id}'
    )

def restro_detail(request,category,subcategory):
    if not subcategory:
        message=f"Showing all items in {category}"
    else:
        message=f"Showing {subcategory} in {category}"

    return HttpResponse(message)


def aboutus(request):
    context={
        "name":"Gowher",
        "Course":"Django",
        "Semester":7,
        "Marks":50
    }
    return render(request,"aboutus.html",context)
