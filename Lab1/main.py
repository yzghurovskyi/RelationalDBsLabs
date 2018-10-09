import npyscreen

from dbManager import FootballDatabase
from forms.FindPlayer import FindPlayer
from forms.EditTournament import EditTournament
from forms.EditClub import EditClub
from forms.ClubsList import ClubsListDisplay
from forms.EditPlayer import EditPlayer
from forms.EntityList import EntityListDisplay
from forms.PlayersList import PlayersListDisplay
from forms.TournamentsList import TournamentsListDisplay


class FootballDBApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.database = FootballDatabase()
        self.database.connect()
        # self.database.drop_tables()
        # self.database.create_tables()
        self.addForm("MAIN", EntityListDisplay)
        self.addForm("PLAYERSLIST", PlayersListDisplay)
        self.addForm("EDITPLAYER", EditPlayer)
        self.addForm("CLUBSLIST", ClubsListDisplay)
        self.addForm("EDITCLUB", EditClub)
        self.addForm("TOURNAMENTSLIST", TournamentsListDisplay)
        self.addForm("EDITTOURNAMENT", EditTournament)
        self.addForm("ADVANCEDSEARCH", FindPlayer)

    def onCleanExit(self):
        self.database.close_connection()


if __name__ == '__main__':
    myApp = FootballDBApplication()
    myApp.run()
