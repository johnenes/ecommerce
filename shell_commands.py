from tags.models import Tag


qs = Tag.objects.all()
black = Tag.objects.last()
black.title
black.slug
black.products
"""
Returns:
<django.db.models.field.related_discriptors.create_forward_many_to_many_manger.<locals>.ManyToManyField
"""
black.products.all()
"""
This is an actual queryset of PRODUCT
much like product.objects.all()
but in this case it's all of the prodcuts are the related to the 'black' tag
"""
black.products.all().first()
"""
return the first instrance, if any
"""

exit()

"""
shell session 2
"""

qs = Product.objects.all()
print(qs)
tshirt  = qs.first()
tshirt.title
tshirt.description


tshirt.tag
"""
Raise an error becsuse the product model doens't have a field 'tag'
"""
tshirt.tags
"""
Raise an error beacuse the product model doens't have a field tags
"""
tshirt.tag_set
"""
Returns an actual Queryset of the Tag model realted to this Product
<Quseryset [<Tag: T shirt>,<Tag: Tshirt]
"""
 
 
