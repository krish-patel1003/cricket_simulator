
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

After this it will print Team Details, which is basically the players and their stats that are randomly generated and distributed to the teams auto balanced.

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

