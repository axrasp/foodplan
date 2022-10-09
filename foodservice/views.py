from django.shortcuts import render

from foodservice.models import (Allergen, Recipe, RecipeCategory,
                                RecipeIngredient)
from subscription.models import Subscription


def serialize_recipe(recipe):
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    serialized_ingredients = []
    for ingredient in ingredients:
        serialized_ingredients.append({
            'name': ingredient.ingredient.name,
            'quantity': ingredient.ingredient_quantity,
        })
    return {
        'category': recipe.category.name,
        'name': recipe.name,
        'calories': recipe.calories,
        'ingridients': serialized_ingredients,
    }


def selected_recipes(allergen, menu_types):
    return Recipe.objects.order_by('?')[:3]


def card(request):
    context = {
        'selected_recipes': [
            serialize_recipe(recipe) for recipe in selected_recipes(1, 1)
        ]
    }
    return (request, 'card1.html', context)


def get_account(request):
    if not Subscription.objects.filter(client=request.user, status=True).exists():
        context = {
            'subscription_status': 0
        }
        return render(request, template_name="lk.html", context=context)
    sub = Subscription.objects.get(client=request.user, status=True)
    allergens = [allergen.name for allergen in sub.allergens.all()]

    br_ingridients_context = []
    if sub.breakfast:
        breakfast_receipe = RecipeCategory.objects.get(name='Завтрак')\
            .recipes.order_by('?').first()
        breakfast_ingridients = breakfast_receipe.ingredients.all()
        br_ingridients_context = [ingridient.name for ingridient
                                  in breakfast_ingridients]

    context = {
        'subscription': {
            'name': sub.type.name,
            'status': 1,
            'paid_till': sub.paid_till,
            'allergens': allergens,
            'dishes': sub.dishes,
            'breakfast': sub.breakfast,
            'dinner': sub.dinner,
            'supper': sub.supper,
            'desert': sub.desert
        },
        'receipts': {
            'breakfast': {
                'name': breakfast_receipe.name,
                'description': breakfast_receipe.description,
                'ingridients': br_ingridients_context,
                'calories': breakfast_receipe.calories,
            }
        }

    }

    return render(request, template_name="lk.html", context=context)
