import factory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('Pystr')
    slug = factory.Faker('Pystr')
    description = factory.Faker('Pystr')
    active = factory.Iterator(True, False)

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('Pystr')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('Pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product