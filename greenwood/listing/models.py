from django.db import models
from django.db.models.signals import post_save,pre_save
from django_resized import ResizedImageField

class Listing(models.Model):
    title=models.CharField(blank=True,null=True,default=None,max_length=140)
    price = models.IntegerField(default=0,blank=True)
    year = models.IntegerField(blank=True,null=True,default=None)
    fuel=models.CharField(blank=True,null=True,default=None,max_length=140)
    city=models.CharField(blank=True, null=True, default=None, max_length=140)
    odometr=models.CharField(blank=True,null=True,default=None,max_length=140)
    volume=models.CharField(blank=True,null=True,default=None,max_length=140)
    model=models.CharField(blank=True,null=True,default=None,max_length=140)
    image_url=models.CharField(blank=True,null=True,default=None,max_length=500)
    listing_link=models.CharField(blank=True,null=True,default=None,max_length=500)
    is_active = models.BooleanField(default=True)
    is_main= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image_uploaded = ResizedImageField(size=[320, 240],quality=100,upload_to='listings_imgs',  null=True) #можно через PIllow




    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name='Listing'
        verbose_name_plural= 'Listings'

#
#
# class ListingImage(models.Model):
#
#     listing=models.ForeignKey(Listing,blank=True,null=True,default=None,on_delete=models.CASCADE)
#     image=models.ImageField(upload_to='listings_imgs/',default=None,blank=True,null=True)
#     is_main=models.BooleanField(default=False)
#
#
#
#     def __str__(self):
#         return f'{self.id}'
#
#     class Meta:
#         verbose_name='Image'
#         verbose_name_plural= 'Images'
# #
# #
# def listing_id_to_image(sender,instance,created,**kwargs):
#     # print(instance)
#
#     # id=instance.id
#     # print('id',id)
#     # instance.listin=
#     # instance.save(force_update=True)
#     listing=instance.id
#     print(listing)
#     instance=ListingImage.listing
#     # print(instance)
#     instance=listing
#     print(instance)
#     instance.save(force_update=True)
#
#
# post_save.connect(listing_id_to_image,Listing)


# def image_id(instance,**kwargs):
#     print('ps',instance.id,instance)
#
#     return instance.id
#
#
# def listing_ids(sender,instance,created,**kwargs):
#     print('inst',instance)
#     listing=instance.id
#     print('lis',listing)
#     all_photos_in_listing = ListingImage.objects.filter(listing=listing)
#     print('all',all_photos_in_listing)
#
#
#     # order_total_price = 0
#     # for item in all_products_in_order:
#     #     order_total_price += item.amount
#     items=[]
#     for item in all_photos_in_listing:
#         print("item",item)
#         items.append(item)
#     return items
#
#
#     # instance.order.order_total_price=order_total_price
    # instance.order.save(force_update=True)

# post_save.connect(image_id,ListingImage)
# post_save.connect(listing_id,Listing)

