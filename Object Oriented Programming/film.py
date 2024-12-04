class Movie:
    title:str
    rating:float
    run_time:float
    director:str
    genre:str
    
    
    def set_movie(self,title,rating,run_time,director,genre):
        
        self.title=title
        
        self.rating=rating
        
        self.run_time=run_time
        
        self.director=director
        
        self.genre=genre
        
    def display_movie(self):
        print(self.title,self.rating ,self.run_time,self.director,self.genre)
        
film_1=Movie()
film_2=Movie()
film_1.set_movie("ARM",8.5,140,"Jithin Lal","Fictional")
film_2.set_movie("KGF",9,150,"Raja Mouly","Action")

film_1.display_movie()
film_2.display_movie()