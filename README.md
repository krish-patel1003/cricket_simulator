
# Crickect Simulator



## Run Locally

Clone the project

```bash
  git clone https://github.com/krish-patel1003/cricket_simulator.git
```

Go to the project directory

```bash
  cd cricket_simulator
```

Execute

```bash
  python app.py
```


## Initializing Match

When you execute the app.py file, it will ask some questions about the field, team, toss.

First question is the name of the field, entering the name it simulator will generate a random field.

```bash
Let's prepare the match!
Enter the field name:   
```
for example, let's say we enter "Lord's"

```bash
Let's prepare the match!
Enter the field name: Lord's
Field Details:  {'field_name': "Lord's", 'field_size': 69, 'fan_ratio': '1:1', 'pitch_conditions': 'dusty', 'home_advantage': 1}
```

Next question is going to be, to select team names. For example, India and England

```bash
Enter Team A name: India
Enter Team B name: England
```

After this it will print Team Details, which is basically the players and their stats that are randomly generated and distributed to the teams.

Next it will ask one of the team to choose heads or tails for the toss. for heads enter 0 and for tails enter 1.

```bash
India Choose heads(0) or tails(1): 0
```

Next who ever wins the toss, will choose to bat or bowl first. for choosing batting enter 0 and for bowling enter 1.

```bash
England Choose bat(0) or bowl(1): 1
```

Next question is how many are to be played in the match. For example, 3

```bash
Enter the number of overs: 3
```

After entering all these details and the match will start and for all the over ball by ball details will be displayed. At the end the match result will be displayed.

## Methodology 

#### Choosing Captain
Method: Average of the individual players skill is compared with other players and the one with the highest average is selected as the captain.

#### Choose Bowler
Method: Sorted list of players on the basis of bowling skill is used. The sorted list is then used as round robin to choose a bowler for a over.

#### Choose Batting Order and Next Batsman
Method: Sorted list of players on the basis of batting skill. As the players get out the next in the list gets to the field.

#### Ball result
Method: There is a fixed list of ball results ["out", "wide", "no ball", "dot", "1 run", "2 runs", "3 runs", "4 runs", "6 runs"]. 

1. skill_difference = batsman.batting_skill - bowler.bowling_skill
2. random_result = random(float(0.0, 1.0)) 
3. result_probability = skill_difference * random_result

random_result is to randomize result on the basis of the probabilty of a ball result and product which is used to generate a index for ball_result_types array to give a ball_result.

If the ball result from this is in ["1 run", "2 runs", "3 runs"] the probability is multiplied with the batsman.running_skill to improve the prediction of ball result.

If the ball result is "out" then the result is first randomized to types in which a player can get out [ "caught", "bowled", "run out", "stumped", "lbw" ].

If the player is caught out then bowling team's fielding average is used to make final decision.

If the player is run out then both batsmen running skill average is used to determine the final decision.

