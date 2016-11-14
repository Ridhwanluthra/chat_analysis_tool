class yass_stemmer(object):

	#function just returns the penalty if not match
	def pi(self, ch1, ch2):
		if ch1 == ch2:
			return 1
		else:
			return 0

	def string_distance_measures(self, str1, str2):
		n = min(len(str1), len(str2))
		d1 = 0
		first_mismatch = False
		# used m in range due to usage in text
		for m in range(0,n):
			penalty = self.pi(str1[m], str2[m])
			d1 += penalty/2**m
			if penalty == 1 and first_mismatch = False:
				common_sum = 0
				for i in range(m, n):
					common_sum += 1/2**(i-m)
				if m > 0:
					d2 = common_sum/m
					d3 = common_sum*(n-m+1)/m
				else:
					d2 = float('Inf')
					d3 = float('Inf')
				d4 = common_sum*(n-m+1)/(n+1)
				first_mismatch = True
		return d1, d2, d3, d4
	