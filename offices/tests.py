from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import inspect


# Create your tests here.
# python manage.py test offices

class OfficeTestFT(StaticLiveServerTestCase):

	# fixtures is the same as getting data and in this case we get it from a json file
	# Created by python manage.py dumpdata offices.office --indent=2 > offices/fixtures/offices.json
	fixtures = ['offices.json']

	def setUp(self):
		# self.browser is the selenium object which represents the web browser, aka the WebDriver.
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def _setup_gotoOfficeListPage(self):
		# User goes to the homepage
		self.browser.get(self.live_server_url) # .get is tells the browser to go to a new page
		time.sleep(2)
		# User clicks the Offices link
		office_link = self.browser.find_element_by_id('offices-link')
		office_link.click()
		time.sleep(1)
		# System makes sure that he is redirected to the Office List Page
		h2 = self.browser.find_element_by_tag_name("h2")
		self.assertEquals(h2.text, 'List of Offices')
		# System makes sure that there is a list of offices
		# START User checks if values are present in the table
		tr = self.browser.find_elements_by_tag_name("tr")
		td = tr[1].find_elements_by_tag_name("td")
		self.assertIn('United Kingdom', td[0].text)
		self.assertIn('EU', td[1].text)
		# END User checks if values are present in the table

	def test_gotoOfficeListPage(self):
		# User goes to the Office List Page
		self._setup_gotoOfficeListPage()
		print ("------------")
		print ("%s.%s DONE" % (self.__class__.__name__, inspect.stack()[0][3]))

	def test_gotoOfficeDetailPage(self):
		# User goes to the Office List Page
		self._setup_gotoOfficeListPage()
		# User clicks an office
		tr = self.browser.find_elements_by_tag_name("tr")
		td = tr[1].find_elements_by_tag_name("td")
		a = td[0].find_element_by_tag_name("a")
		a.click()
		# System makes sure that there is two details of the office
		container = self.browser.find_element_by_css_selector(".container")
		h1 = container.find_element_by_tag_name("h1")
		self.assertEquals("United Kingdom", h1.text)
		h4 = container.find_elements_by_tag_name("h4")
		self.assertEquals(2, len(h4))
		# System makes sure that Currency Details are there
		print ("---")
		self.assertIn("Currency", h4[0].text)
		self.assertIn("EU", h4[0].text)
		# System makes sure that the Client Details are there
		self.assertIn("Clients", h4[1].text)
		ul = self.browser.find_elements_by_tag_name("ul")
		self.assertEquals(2, len(ul))
		
		print ("------------")
		print ("%s.%s DONE" % (self.__class__.__name__, inspect.stack()[0][3]))


