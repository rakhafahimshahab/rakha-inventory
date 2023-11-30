from django.test import TestCase,Client

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_show_main(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

        self.assertEqual(response.context['application_name'], 'Pirates Database')
        self.assertEqual(response.context['name'], 'Rakha Fahim Shahab')
        self.assertEqual(response.context['class'], 'PBP KI')
