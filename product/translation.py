from modeltranslation.translator import translator, TranslationOptions
from .models import Products,ProductsCategory, color, city


class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class NewsTranslationOptions1(TranslationOptions):
    fields = ('name',)
class rang23(TranslationOptions):
    fields = ('rang',)



translator.register(Products,NewsTranslationOptions)
translator.register(color,rang23)

translator.register(ProductsCategory,NewsTranslationOptions1)



