import urllib
from bs4 import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("http://www.genentech-access.com/hcp/find-support-program/authorized-distributors").read()
# print htmltext

soup = BeautifulSoup(htmltext)
soup_product_list =  soup.find("ul", { "class" : "generic-authorized-distributor" })
soup_products = soup_product_list.contents

global_map = {}
# This prints out a list of 18 products.
# Name of product
for product in soup_products:
	try:
		product_name =  product.find('span', { "class" : "generic-authorized-distributor-title" })
		product_name = product_name['id']
		# print product_name	
		global_map[product_name] = {}

		soup_dist_categories =  product.findAll("div", { "class" : "node" })
		# print soup_dist_categories

		for dist_category in soup_dist_categories:
			# This is the type of dists that are available for the products
			dist_category = dist_category.contents
			# print dist_category
			dist_category_subchildren = dist_category[3] # This is all the content under this category.
			dist_category_subchildren = dist_category_subchildren.findAll('td') # Creates a list of each specific dist.
			dist_category = dist_category[1] # This is the name of the category of distributor.
			# print dist_category
			dist_type = dist_category.contents[2].replace("\n","").replace("\r","") # Clean up the name of the category.

			global_map[product_name][dist_type] = {}

			specific_dist_list = []
			for specific_dist in dist_category_subchildren:
				# This is going to be associated with the type of dist
				specific_dist = specific_dist.contents # You could do .string or .contents here.  .string would exlude thigns inside an <a> tag.
				# print specific_dist
				# print str(product_name) + ", " + str(dist_type) + ", " + specific_dist + "\n"
				specific_dist_list.append(specific_dist)

			global_map[product_name][dist_type] = specific_dist_list


			
	except:
		print "dist_category"

print global_map



