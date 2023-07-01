from random import choice


class T2cup:
    allTeam = []
    def entry_teme(self, team):
        self.allTeam.append(team)


class Team(T2cup):
    def __init__(self, team_name):
        self.team_name = team_name
        self.palayersListOfObj = []
        super().entry_teme(self)

    def entry_players(self, player):
        self.palayersListOfObj.append(player)

    def __repr__(self) -> str:
        return f"Team Name: {self.team_name}"

class Player:
    def __init__(self, name, teamobj):
        self.name = name
        self.strikeRate = 0.0
        self.run_bat = 0
        self.ballUsed = 0
        self.sixs = 0
        self.fours = 0
        self.run_ball = 0
        self.wicketsTaken = 0
        self.ballsbowled = 0
        teamobj.palayersListOfObj.append(self)

    def __repr__(self) -> str:
        return f"Name: {self.name}"

class Innings:
    def __init__(self, team1_obj, team2_obj, batting_team_obj, balling_team_obj):
        self.teamOneObj = team1_obj
        self.teamTwoObj = team2_obj
        self.batting_team = batting_team_obj
        self.balling_team = balling_team_obj
        self.totalrun = 0
        self.totalwicket = 0
        self.currentball = 0
        self.totalOver = 0
        self.currentBattingList = [batting_team_obj.palayersListOfObj[0],batting_team_obj.palayersListOfObj[1]]
        self.stiket = batting_team_obj.palayersListOfObj[0]
        self.currentBowler = None
        self.currentOver_status = []
        self.allOverStatus = []
        
    def show_score_bord(self):
        print(f'*{self.currentBattingList[0].name} {self.currentBattingList[0].run_bat}  ({self.currentBattingList[0].ballUsed})')
        print(f'{self.currentBattingList[1].name} {self.currentBattingList[1].run_bat}  ({self.currentBattingList[1].ballUsed})')
        print(f'{batting_team.team_name[:3].upper()} | {self.totalrun} - {self.totalwicket}')
        print(f'{self.totalOver}.{self.currentball}')
        if self.currentBowler is not None:
            print(f'{self.currentBowler.name} - {self.currentBowler.run_ball} / {self.currentBowler.wicketsTaken}')

    def set_bowler(self, bowlwrObj):
        self.currentBowler = bowlwrObj

    def bowl(self, statrs):
        self.totalrun += statrs
        self.stiket.run_bat += statrs
        self.stiket.ballUsed += 1
        self.currentBowler.run_ball += statrs
        self.currentBowler.ballsbowled += 1
        self.currentball += 1
        

cup = T2cup()
bangladesh = Team("Bangladesh")
india = Team("Indea")

sakib = Player("sakib", bangladesh)
tamim = Player("Tamim Iqbal", bangladesh)
musfiq = Player("Musfiqur rahaman", bangladesh)

birat = Player("Virat kohli", india)
rohit = Player("Rohit sarma", india)
bumta = Player("Bumra", india)

while True:
    print("Select your team name")
    for i in range(len(cup.allTeam)):
        print(f"{i+1} : {cup.allTeam[i].team_name}")
    teamOneIndx, teamTwoIndx = map(int,input("Enter two team index :").split(' '))
    teamOneIndx -= 1
    teamTwoIndx -= 1
    teamOneObj = cup.allTeam[teamOneIndx]
    teamTwoObj = cup.allTeam[teamTwoIndx]
    tassWinn = choice([teamOneIndx,teamTwoIndx])
    print(f"{cup.allTeam[tassWinn].team_name} tassWinn")
    if tassWinn == teamOneIndx:
       tassLoss = teamTwoIndx
    else:
        tassLoss = teamOneIndx

    rand = choice([0, 1])
    if rand == 0:
        # winn team choice bowling
        print(f"{cup.allTeam[tassWinn].team_name} choice bowling")
        balling_team = cup.allTeam[tassLoss]
        batting_team = cup.allTeam[tassWinn]
    else:
        # winn team choice bating
        print(f"{cup.allTeam[tassWinn].team_name} choice bating")
        batting_team = cup.allTeam[tassLoss]
        balling_team = cup.allTeam[tassWinn]

    innings = Innings(teamOneObj, teamTwoObj, batting_team, balling_team)
    innings.show_score_bord()
    print("set bowlwr :")
    for i, val in enumerate(balling_team.palayersListOfObj):
        print(f'{i+1} {val.name}')
    bowlerIndx = int(input("Enter bowler Indx :"))
    bowlerIndx -= 1
    bowlerObj = balling_team.palayersListOfObj[bowlerIndx]
    innings.set_bowler(bowlerObj)
    innings.bowl(6)
    innings.show_score_bord()    
 
    break
