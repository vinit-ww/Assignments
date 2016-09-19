from django.contrib import admin

from .models import Category,Product,ProductCategories,ProductImage,Brand
from .models import UserProfile



class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'parent_id', 'created_by','created_date','modified_by','modified_date','status')


    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


    def save_formset(self, request, form, formset, change):
        if formset.model == Category:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(ProductCategories)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(ProductImage)
admin.site.register(Brand)



