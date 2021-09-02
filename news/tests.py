from django.test import TestCase
from .models import Editor, Tag, Article

# Create your tests here.

# editor module test
class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.james = Editor(first_name = 'James', last_name = "Muriuki", email = 'jamesmuriuki@gmail.com')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    # testing save method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # testing delete method
    def test_delete_method(self):
        self.james.delete_editor(self.james.first_name)
        editor = Editor.objects.get(first_name = self.james.first_name)
        print(editor)
        # self.assertTrue(editor is None)