from django.db import models

class ToolItem(models.Model):
	CATEGORY_CHOICES = (
		('WOODSHOP', 'Wood Shop'),
		('FORGE', 'Forge'),
		('3D', '3d Printing'),
		('OTHER', 'Other'),
		('CERAMICS', 'Ceramics'),
		('Kitchen', 'Industrial Kitchen'),
		)

	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=1.00)
	created = models.DateTimeField(auto_now_add=True)
	categories = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other', null=True, blank=True)
	checked = models.BooleanField(default=False)

	def __str__(self):
		return self.name
