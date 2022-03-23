# DO NOT CHANGE THE FUNCTION SIGNATURE IN THE SOLUTION AREA
import numpy as np   
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]



    
gandalf_wins = 0
saruman_wins = 0
tie = 0

gandalf_power = []
saruman_power = []    

winner = []

# Which sorcerer won the battle - Gandalf or Saruman?
def battle():
    # YOUR SOLUTION HERE
    
    
    for wins in range(len(gandalf)):
      gandalf_wins = 0
      saruman_wins = 0
      tie = 0
      
      if gandalf[wins] > saruman[wins]:
        gandalf_wins += 1
      elif gandalf[wins] < saruman[wins]:
        saruman_wins += 1
      else:
        tie += 1
        
    if gandalf_wins > saruman_wins:
      return 'Gandalf wins'
    elif gandalf_wins < saruman_wins:
      return 'Saruman wins'
    else:
      return 'Tie'      
    
#  Average of the spells in the lists? Round off your result to one decimal place.
def avg_spells():
    # YOUR SOLUTION HERE

    gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
    
    saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

    power = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10,
    'Black Tentacles': 25, 
    'Contagion': 45
    }   

    #Adding values to gandalf power
    for i in range(10):
      if gandalf[i] == 'Fireball' in gandalf:
          gandalf_power.append(50)
      elif gandalf[i] == 'Lightning bolt' in gandalf:
          gandalf_power.append(40)
      elif gandalf[i] == 'Magic arrow' in gandalf:
          gandalf_power.append(10)
      elif gandalf[i] == 'Black Tentacles' in gandalf:
          gandalf_power.append(25)
      elif gandalf[i] == 'Contagion' in gandalf:
          gandalf_power.append(45)
      else:
          print("error")

    #Adding values to saruman power
    for i in range(10):
      if saruman[i] == 'Fireball' in saruman:
          saruman_power.append(50)
      elif saruman[i] == 'Lightning bolt' in saruman:
          saruman_power.append(40)
      elif saruman[i] == 'Magic arrow' in saruman:
          saruman_power.append(10)
      elif saruman[i] == 'Black Tentacles' in saruman:
          saruman_power.append(25)
      elif saruman[i] == 'Contagion' in saruman:
          saruman_power.append(45)
      else:
          print("error")
    
    #Total of wins for each scorcecer
   

    for x in range(10):
        if saruman_power[x] > gandalf_power[x]:
            winner.append("Saruman")
        elif saruman_power[x] < gandalf_power[x]:
            winner.append("Gandalf")
        else:
            winner.append("Tie")
            
     #Define the winner 
    for i in range(8):
      if winner[i] == winner[i + 1] and winner[i + 1] == winner[i + 2]:
        print(winner[i], "wins")
        break
        
    if winner[i] == "Gandalf":
        mean_winner = np.mean(gandalf_power)
        return "The mean of the winner is", mean_winner.round(1)
    else:
        mean_winner = np.mean(saruman_power)
        return "The mean of the winner is", mean_winner.round(1)


def stdev_spells():
    # YOUR SOLUTION HERE
    import numpy as np

    for i in range(8):
      if winner[i] == winner[i + 1] and winner[i + 1] == winner[i + 2]:
        print(winner[i], "wins")
        break
        
    if winner[i] == "Gandalf":
        mean_winner = np.std(gandalf_power)
        return "The standar deviation of the winner is", mean_winner.round(1)
    else:
        mean_winner = np.std(saruman_power)
        return "The standar deviation of the winner is", mean_winner.round(1)   


#  Standard deviation of the spells in the lists? Round off your result to one decimal place.


print(battle())
print(avg_spells())
print(stdev_spells())