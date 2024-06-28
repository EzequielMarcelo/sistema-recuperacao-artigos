from app.views.article_view import ArticleView
from app.models.article_model import Article
from app.models.user_model import User
from app.database.database import Database

class ArticleController:
    def __init__(self, database:Database):
        self.database = database
        self.view = ArticleView()
    
    def display_menu(self):
        self.view.display_menu()    
   
    def get_user_choice(self):
        return self.view.get_user_choice()    
    
    def display_message(self, message):
        self.view.display_message(message)
    
    def set_current_user(self, user:User):
        self.current_user = user

    def arxiv_search(self):
        cpf = self.current_user.cpf
        query, max_results = self.view.get_search_parameters()
        articles_xml = Article.search_arxiv(query, max_results)
        parsed_articles = Article.parse_arxiv_response(articles_xml)
        
        if articles_xml:
            for article in parsed_articles:
                article_data = (article['id'], article['title'], article['summary'], article['link'], cpf, query)
                self.database.add_article(article_data)
        

