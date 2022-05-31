from django.conf import settings
from django.db import models
from django.utils import timezone
from matplotlib.pyplot import table

import numpy as np

# Create your models here.

class Calculator(models.Model):
	a_credit		= models.PositiveIntegerField()		# credit amount
	r_inter			= models.FloatField(max_length=5)				# interest rate
	a_annuity 		= models.PositiveIntegerField()		# yearly amount to pay
	r_repay			= models.FloatField(max_length=5)				# repayment rate
	n_credit_term	= models.PositiveIntegerField()		# credit term

#	data = np.array([[]])

	def calculate_financing(self):
		BMI = 	[['Asterix','Majestix','Miraculix','Obelix','Troubadix'],
				[ 9.2 , 20.0 , 13.3 , 49.9 , 6.4 ]]
		return BMI

	def print_financing(self):
		pass