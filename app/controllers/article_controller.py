from app.views.article_view import ArticleView

class ArticleController:
    def __init__(self):
        self.view = ArticleView()
    
    def display_menu(self):
        self.view.display_menu()    
   
    def get_user_choice(self):
        return self.view.get_user_choice()    
    
    def display_message(self, message):
        self.view.display_message(message)

    def arxiv_search(self):
        query, max_results = self.view.get_search_parameters()
        

