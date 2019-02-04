# This program creates a list of suggested movies for the user based on the 
# information inputted by the user about preferred original language, 
# preferred dubbed language, and genre of movie
# by Kristin Albright, Mika Cooney, and Jack Daley

import csv
from tkinter import *

class Survey:
    """ 
    This class creates an object Survey that opens a tkinter 
    window and asks a series of preference questions. 
    
    The instance variables include language, dubLanguage, and 
    prefKeyList. 
    
    Language is a string that is initiated as empty, but changed 
    by the button the user clicks (changed to either 'fr' to 
    represent French, 'en' to represent English, or 'es' to represent 
    Spanish). 
    
    DubLanguage is a string that is initiated as empty, but 
    is changed by the button the user clicks (changed
    to either 'fr' to represent French, 'en' to represent 
    English, or 'es' to represent Spanish). 
    
    PrefKeyList is a list that is initialized as empty, but 
    appended to add the genre types that the user selects 
    ("Adventure", "Drama", "Family", "Animation", "Comedy", 
    "Fantasy", "Romance", "Horror", "Science Fiction"). 
    """
    
    def __init__(self):
        self.language = ""
        self.dubLanguage = ""
        self.prefKeyList = []
        
        prefLang = self.language
        prefDubLang = self.dubLanguage
        prefKey = self.prefKeyList
        
    def choose1Lang(self, language):
        """ 
        choose1Lang takes chosenLang1, a string, as a 
        parameter which is given by the original language 
        buttons. 
        
        Returns: self.language (which updates the language to
        the one selected by the user in the function drawQ1)
        
        Preconditions: Must be passed a chosenLang1 from the 
        user pressing a button.
        
        Postconditions: self.language is updated to the language
        selected by the user. 
        """
        
        if language == "French": 
            self.language = "fr"
            return self.language
        elif language == "English": 
            self.language = "en"
            return self.language
        elif language == "Spanish": 
            self.language = "es"
            return self.language
            
    def choose2Lang(self, dubLanguage):
        """ 
        choose2Lang takes chosenLang2, a string, as a 
        parameter which is given by the dubbed language 
        buttons. 
        
        Returns: self.dubLanguage (which updates the dubLanguage to
        the one selected by the user in the function drawQ2andQ3).
        
        Preconditions: Must be passed a chosenLang2 from the 
        user pressing a button.
        
        Postconditions: self.dubLanguage is updated to the language
        selected by the user. 
        """
        
        if dubLanguage == "French": 
            self.dubLanguage = "fr"
            return self.dubLanguage
        elif dubLanguage == "English": 
            self.dubLanguage = "en"
            return self.dubLanguage
        elif dubLanguage == "Spanish": 
            self.dubLanguage = "es"
            return self.dubLanguage
    
    def getPrefLang(self):
        """
        Returns: the preferred original language of the user as a string.
        """
        
        return self.language
    
    def getPrefDubLang(self):
        """
        Returns: the dubbed language of the user as a string.
        """
        
        return self.dubLanguage
    
    def getPrefKey(self):
        """ 
        Returns: the preferred movie keywords of the user as a list of strings.
        """
        
        return self.prefKeyList
    
    
    def recordKey(varList, i):
        """ 
        Updates the status of each of the genre options to either be 
        stored as on or off, based on number of clicks by the user. 
        
        Preconditions: varList is passed in correctly as a list.
        """
        
        varList[i] = 1 - varList[i]
    
    def submit(window, self, Survey, Movie, root, movie, varList):
        """
        Calls compareMovie, defines movie_list as the return of 
        compareMovie, calls the function drawAllMovies and edits 
        preKeyList
        
        Preconditions: The parameters are passed in correctly
        """
        
        global movie_list
        counter = 0
        
        #Initializing a list of possible keywords
        keyList = ["Adventure", "Drama", "Family", "Animation", "Comedy", "Fantasy", "Romance", "Horror", "Science Fiction"]
                
        for i in range(len(varList)):
            if varList[i] == 1:
                self.prefKeyList.append(keyList[i])
                
        prefLang = self.getPrefLang()
        prefDubLang = self.getPrefDubLang()
        prefKeyList = self.getPrefKey()
                
        movie_list = compareMovie(prefKeyList, prefDubLang, prefLang, Movie, Survey)
        movie.movieList = movie_list
        
        top = ""
        backSelect = 0
        
        drawAllMovies(root, movie_list, counter, top, movie, backSelect)
        
    def drawQ1andQ2andQ3(self, window, root, Survey, Movie, movie):
        """ 
        Creates the survey questions and buttons that allow the user to specify 
        their preferred original language, dubbed language, and genre(s).
        
        Preconditions: the parameters are passed in correctly.
        """
        
        window.pack()
        
        Welcometxt = window.create_text(60,25,fill="black",text="Pick an Original" + "\n" + "Language:")

        button1 = Button(root,text = "French",command=lambda: Survey.choose1Lang(self, "French"))
        button1.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button1_window = window.create_window(20, 50, anchor=NW, window=button1)
        button1.update()
        
        button1 = Button(root,text = "French",command=lambda: Survey.choose1Lang(self, "French"))
        button1.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button1_window = window.create_window(20, 50, anchor=NW, window=button1)
        button1.update()

        button2 = Button(root,text = "English",command=lambda: Survey.choose1Lang(self, "English"))
        button2.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button2_window = window.create_window(20, 100, anchor=NW, window=button2)
        button2.update()

        button3 = Button(root,text = "Spanish",command=lambda: Survey.choose1Lang(self, "Spanish"))
        button3.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button3_window = window.create_window(20, 150, anchor=NW, window=button3)
        button3.update()
        
        Welcometxt = window.create_text(200,25,fill="black",text="Pick a Dubbed" + "\n" + "Language:")

        button1 = Button(root,text = "French",command=lambda: Survey.choose2Lang(self,"French"))
        button1.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button1_window = window.create_window(162, 50, anchor=NW, window=button1)
        button1.update()

        button2 = Button(root,text = "English",command=lambda: Survey.choose2Lang(self,"English"))
        button2.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button2_window = window.create_window(162, 100, anchor=NW, window=button2)
        button2.update()

        button3 = Button(root,text = "Spanish",command=lambda: Survey.choose2Lang(self,"Spanish"))
        button3.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button3_window = window.create_window(162, 150, anchor=NW, window=button3)
        button3.update()
        
        button4 = Button(root,text = "Submit",command=lambda: Survey.submit(window, self, Survey, Movie, root, movie, varList))
        button4.configure(width = 0, activebackground = "#D2D2D2", relief = GROOVE)
        button4_window = window.create_window(91, 175, anchor=NW, window=button4)
        button4.update()
        
        #Initializing a variable list to track the state of check-boxes (0 = F ; 1 = T)
        varList = [0,0,0,0,0,0,0,0,0]
        
        #Intializing checkboxes
        Label(root, text="What Kind of Movie?").pack()
        Checkbutton(root, text="Adventure", variable=IntVar(), command=lambda: Survey.recordKey(varList, 0)).pack()
        Checkbutton(root, text="Drama", variable=IntVar(), command=lambda: Survey.recordKey(varList, 1)).pack()
        Checkbutton(root, text="Family", variable=IntVar(), command=lambda: Survey.recordKey(varList, 2)).pack()
        Checkbutton(root, text="Animation", variable=IntVar(), command=lambda: Survey.recordKey(varList, 3)).pack()
        Checkbutton(root, text="Comedy", variable=IntVar(), command=lambda: Survey.recordKey(varList, 4)).pack()
        Checkbutton(root, text="Fantasy", variable=IntVar(), command=lambda: Survey.recordKey(varList, 5)).pack()
        Checkbutton(root, text="Romance", variable=IntVar(), command=lambda: Survey.recordKey(varList, 6)).pack()
        Checkbutton(root, text="Horror", variable=IntVar(), command=lambda: Survey.recordKey(varList, 7)).pack() 
        Checkbutton(root, text="Science Fiction", variable=IntVar(), command=lambda: Survey.recordKey(varList, 8)).pack()
        
        root.mainloop()

class Movie:
    """ This class creates an object Movie that reads and returns all
    of the necessary data about the movie for this program. 
    
    The instance variables include ogLanguage, ogDubLang, ogKeyWords, 
    and movieList. 
    
    ogLanguage is initiated as an empty string but is later edited to equal
    the specific movie's original language. 
    
    ogDubLang is initialized as an empty string but is later edited to 
    equal the dubbed language(s) of the specific movie. 
    
    ogKeyWords is initialized as an empty list but is later appended to 
    include all genres that the user selects for their movie.
    
    movieList is initialized as an empty list, but is later appended to 
    include all of the movies that fit the user's specifications.
    """
    
    def __init__(self):
        self.ogLanguage = ""
        self.ogDubLang = ""
        self.ogKeyWords = []
        self.movieList = []
        ogLang = self.ogLanguage
        ogDubLang = self.ogDubLang
        ogKeyWords = self.ogKeyWords
    
    def getOgLang(self):
        """
        Returns: the original language of the movie as a string.
        """
        
        return self.ogLanguage
    
    def getOgDubLang(self):
        """
        Returns: the dubbed languages of the movie as a list of strings.
        """
        
        return self.ogDubLang
    
    def getOgKeyWords(self):
        """
        Returns: the keywords of the movie as a list of strings.
        """
        
        return self.ogKeyWords
    
    def getMovieList(self):
        """
        Returns: the list of matched movies.
        """
        
        return self.movieList
    
    def findOgLang():
        """
        Opens up the movies_metadata csv file and isolates the orinial languge
        of the movie
        
        Returns: original_language, a list that holds all of the original 
        languages of the movie list
        """
        
        with open('movies_metadata.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            original_language = []
            next(spamreader)
            for row in spamreader:
                path = row[7]
                original_language.append(path)
        return original_language
    
    def findOgKey():
        """
        Opens up the movies_metadata csv file and isolates the genres that
        the movie falls under.
        
        Returns: a list original_keys that contains a list of genres for 
        each of the movies in the dataset
        """
        
        with open('movies_metadata.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            original_keys = []
            next(spamreader)
            for row in spamreader:
                if len(row) > 3:
                    if len(row[3]) > 0:
                            path = eval(row[3])
                            small_list = []
                            for item in path:
                                key = item['name']
                                small_list.append(key)
                            original_keys.append(small_list)
        return original_keys
    
    def findDubLang():
        """
        Opens up the movies_metadata csv file and isolates the spoken langauges
        that each movie has (dubbed versions of the movie)
        
        Returns: a list dubbed_language that contains a list of the dubbed languages
        for each movie in the dataset
        """
        
        with open('movies_metadata.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            dubbed_language = []
            next(spamreader)
            for row in spamreader:
                if len(row) > 17:
                    if len(row[17]) > 0:
                            path = eval(row[17])
                            small_list = []
                            for item in path:
                                key = item['iso_639_1']
                                small_list.append(key)
                            dubbed_language.append(small_list)
                else:
                    dubbed_language.append([])
        return dubbed_language
        

def compareMovie(prefKeyList, prefDubLang, prefLang, Movie, Survey):
    """
    Compares the results of the survey to the entire list of movies from the 
    movies_metadata csv file.
    
    Returns: rec_movie, a list of all movies that fit all survery conditions
    
    Preconditions: All parameters must be passed in correctly
    """
    
    original_language = Movie.findOgLang()
    dubbed_language = Movie.findDubLang()
    original_keys = Movie.findOgKey()
    rec_movie = []
    i = 0
    with open('movies_metadata.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        while i < len(original_language):
            for row in spamreader:
                if original_language[i] == prefLang and any(dubbed_language[i][n] == prefDubLang for n in range(len(dubbed_language[i]))):
                    for j in original_keys[i]:
                        if j in prefKeyList:
                            rec_movie.append(row[8])
                i = i + 1
    return rec_movie
        
def drawAllMovies(root, movie_list, counter, top, movie, backSelect):
    """
    Creates a window of the first five movies once the survey has been 
    submitted. Includes a next, back and quit button that allow the 
    user to navigate between the list of movies.
    
    Preconditions: All parameters are submitted correctly
    """

    if counter > 0 or backSelect == 1:
        top.destroy()
        top = Toplevel()
        top.title("Here Are Your Movies:")
    else:
        top = Toplevel()
        top.title("Here Are Your Movies:")
    
    backSelect = 0
    
    if len(movie_list) == 0:
        var = StringVar()
        label = Message(top, textvariable=var, relief=FLAT )

        var.set("End of Movie List")
        label.pack()
    else:
        button1 = Button(top, text=movie_list[0], command=lambda: drawSum(movie_list[0]))
        button1.pack()
        button2 = Button(top, text=movie_list[1], command=lambda: drawSum(movie_list[1]))
        button2.pack()
        button3 = Button(top, text=movie_list[2], command=lambda: drawSum(movie_list[2]))
        button3.pack()
        button4 = Button(top, text=movie_list[3], command=lambda: drawSum(movie_list[3]))
        button4.pack()
        button5 = Button(top, text=movie_list[4], command=lambda: drawSum(movie_list[4]))
        button5.pack()
        buttonNext = Button(top, text="Next", command=lambda: drawAllMovies(root, movie_list[5:], counter+1, top, movie, backSelect))
        buttonNext.pack()
        buttonBack = Button(top, text="Back", command=lambda: drawAllMovies(root, movie.getMovieList()[(5*counter-5):], counter-1, top, movie, backSelect+1))
        buttonBack.pack()
        buttonQuit = Button(top, text="Quit", command=lambda: exit())
        buttonQuit.pack()
        
    mainloop()

def drawSum(movie_name):
    """ 
    A helper function that is used in drawAllMovies to open the summary once the user
    clicks on a button with the title of the movie
    
    Preconditions: movie_name is passed correctly in
    """
    
    sumMov = Toplevel()
    sumMov.title("Summary")
    with open('movies_metadata.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            original_language = []
            next(spamreader)
            for row in spamreader:
                if row[8] == movie_name:
                    path = row[9]
                    var = StringVar()
                    label = Message(sumMov, textvariable=var, relief=FLAT )

                    var.set(path)
                    label.pack()
                    mainloop

        
def main():
    
    #Initializing a window, specifically a tkinter window that allows for buttons
    root=Tk()
    window = Canvas(root)
    root.title('Dubbed Movie Finder')
    
    #Initializing an instance of our two primary classes: Survey and Movie.
    userPrefs = Survey()
    sugMovie = Movie()
    
    Survey.drawQ1andQ2andQ3(userPrefs, window, root, Survey, Movie, sugMovie)

    
main()