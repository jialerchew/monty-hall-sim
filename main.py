import random

def run_trial(switch_door,ndoors=3):
    """
    Runs a single instance of the Monty Hall problem with ndoors doors

    Parameters:
    switch_door : bool
        Whether to switch door after revealing a wrong door. 'True' to switch.
    ndoors      : int, optional
        Number of doors to simulate

    Returns:
    bool
        Outcome of the guess, if user managed to guess the door with prize
    """

    # Randomize prize door and door chosen by participant
    prize_door = random.randint(1,ndoors)
    chosen_door = random.randint(1,ndoors)

    if ndoors < 3:
        print('Must be at least 3 doors!')
        return

    if switch_door:
        # Create list of doors that can be revealed by host
        revealable_doors = list(range(1,ndoors+1))
        revealable_doors.remove(prize_door)
        if prize_door != chosen_door:
            revealable_doors.remove(chosen_door)
        
        # Host reveals one random door from the doors that do not contain the prize
        revealed_door = random.choice(revealable_doors)

        # Create list of doors that participants can switch to
        remaining_doors = list(range(1,ndoors+1))
        remaining_doors.remove(revealed_door)
        remaining_doors.remove(chosen_door)

        # Participant switches choice
        chosen_door = random.choice(remaining_doors)

    return chosen_door == prize_door

def batch_trial(ntrials, switch_door, ndoors=3):
    """
    Runs ntrials iterations of the Monty Hall problem with ndoors doors

    Parameters:
    ntrials     : int
        Number of iterations
    switch_door : bool
        Whether to switch door after revealing a wrong door. 'True' to switch.
    ndoors      : int, optional
        Number of doors to simulate

    Returns:
    bool
        Outcome of the guess, if user managed to guess the door with prize
    """

    if ndoors < 3:
        print('Must be at least 3 doors!')
        return

    # Run the simulation ntrial times and sum the number of wins
    nwins = 0
    for i in range(ntrials):
        if run_trial(switch_door,ndoors):
            nwins += 1

    print(f"Iterated count  : {ntrials}\n"
          f"Switching       : {switch_door}\n"
          f"Win probability : {nwins/ntrials:.2%}\n")

"""
Edit parameters here
min_doors   : int
    Minimum number of doors to start the simulation with
max_doors   : int
    Maximum number of doors before stopping the simulation
iters       : int
    Number of iterations for each door/switch combination
"""
min_doors = 3
max_doors = 10
iters = 5000000

for doornum in range(min_doors,max_doors+1):
    print(f"Number of doors : {i}\n")
    batch_trial(iters,False,doornum)
    batch_trial(iters,True,doornum)