from django.test import TestCase
from .models import Editor, Tag, Article
import datetime as dt

# Create your tests here.

# editor module test
# class EditorTestClass(TestCase):

    # set up method
    # def setUp(self):
    #     self.james = Editor(first_name = 'James', last_name = "Muriuki", email = 'jamesmuriuki@gmail.com')

    # # testing instance
    # def test_instance(self):
    #     self.assertTrue(isinstance(self.james, Editor))

    # # testing save method
    # def test_save_method(self):
    #     self.james.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

    # testing delete method
    # def test_delete_method(self):
    #     self.james.delete_editor(self.james.first_name)
    #     editor = Editor.objects.get(first_name = self.james.first_name)
    #     print(editor)
    #     # self.assertTrue(editor is None)

# artlicle tests
class ArticleTestClass(TestCase):
    
    def setUp(self) -> None:
        # create a new editor and save to db
        self.james = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # createa new tag and save
        self.new_tag = Tag(name = 'testing')
        self.new_tag.save()

        # create new article and save
        self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james) 

        self.new_article.tags.add(self.new_tag)

    def tearDown(self) -> None:
        Editor.objects.all().delete()
        Tag.objects.all().delete()
        Article.objects.all().delete()

    # # test fetching todays news
    # def test_get_todays_news(self):
    #     today_news = Article.todays_news()
    #     self.assertTrue(len(today_news) > 0)

    # 
    # def test_get_news_by_date(self):
    #     test_date = '2017-03-17'
    #     date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    #     news_by_date = Article.days_news(date)
    #     self.assertTrue(len(news_by_date) == 0)