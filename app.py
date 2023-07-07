import models.players as players
import  models.teams as teams
import models.fields as fields
import models.matchs as matchs


def main():

    # Create teams, field, and match objects
    team1 = teams.Team("Team A")
    team2 = teams.Team("Team B")
    field = fields.Field("Field Name", 0.8, "Good", 0.1)
    match = matchs.Match(team1, team2, field)


# Start the match
matchs.start_match()




if __name__ == '__main__':
    main()




