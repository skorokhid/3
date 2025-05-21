from django.test import TestCase
from .models import Category, Recipe

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Desserts")
        self.assertEqual(list(self.category), list("Desserts"))

class RecipeTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Dishes")
        self.recipe = Recipe.objects.create(
            title="Pasta",
            description="Delicious pasta dish",
            instructions="Cook pasta...",
            ingredients="Pasta, sauce",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Pasta")
        self.assertEqual(self.recipe.category, self.category)