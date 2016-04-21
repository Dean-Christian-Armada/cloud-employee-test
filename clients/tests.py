from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import inspect


# Create your tests here.
# python manage.py test clients

class ClientTestFT(StaticLiveServerTestCase):

	# fixtures is the same as getting data and in this case we get it from a json file
	# Created by python manage.py dumpdata clients.client --indent=2 > clients/fixtures/clients.json
	fixtures = ['offices.json', 'clients.json', 'contacts.json']

	def setUp(self):
		# self.browser is the selenium object which represents the web browser, aka the WebDriver.
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def _setup_gotoClientListPage(self):
		# User goes to the homepage
		self.browser.get(self.live_server_url) # .get is tells the browser to go to a new page
		time.sleep(2)
		# User clicks the Clients link
		client_link = self.browser.find_element_by_id('clients-link')
		client_link.click()
		time.sleep(1)
		# System makes sure that he is redirected to the Client List Page
		h2 = self.browser.find_element_by_tag_name("h2")
		self.assertEquals(h2.text, 'List of Clients')
		# System makes sure that there is a list of clients
		# START User checks if values are present in the table
		tr = self.browser.find_elements_by_tag_name("tr")
		td = tr[1].find_elements_by_tag_name("td")
		self.assertIn('Cloud Employee', td[0].text)
		self.assertIn('United Kingdom', td[1].text)
		self.assertIn('2', td[2].text)
		# END User checks if values are present in the table

	def test_gotoClientListPage(self):
		# User goes to the Client List Page
		self._setup_gotoClientListPage()
		print ("------------")
		print ("%s.%s DONE" % (self.__class__.__name__, inspect.stack()[0][3]))

	def test_gotoClientDetailPage(self):
		# User goes to the Client List Page
		self._setup_gotoClientListPage()
		# User clicks an client
		tr = self.browser.find_elements_by_tag_name("tr")
		td = tr[1].find_elements_by_tag_name("td")
		a = td[0].find_element_by_tag_name("a")
		a.click()
		# System makes sure that there is two details of the client
		container = self.browser.find_element_by_css_selector(".container")
		h1 = container.find_element_by_tag_name("h1")
		self.assertEquals("Cloud Employee", h1.text)
		h4 = container.find_elements_by_tag_name("h4")
		self.assertEquals(2, len(h4))
		# System makes sure that Currency Details are there
		print ("---")
		self.assertIn("Office", h4[0].text)
		self.assertIn("United Kingdom", h4[0].text)
		# System makes sure that the Client Details are there
		self.assertIn("Contacts", h4[1].text)
		ul = self.browser.find_elements_by_tag_name("ul")
		self.assertEquals(2, len(ul))
		
		print ("------------")
		print ("%s.%s DONE" % (self.__class__.__name__, inspect.stack()[0][3]))


