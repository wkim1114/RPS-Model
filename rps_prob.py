"""Smart RPS machine - Prob Based."""


from random import randint


play_count: int = 0
result: dict[str, int] = {"Rock": 0, "Paper": 0, "Scissor": 0}


def computer_play() -> str:
    """Computer choice."""
    rng = randint(0, 2)
    if rng == 0:
        return "Rock"
    elif rng == 1:
        return "Paper"
    else:
        return "Scissor"


def model_prob_based(p_choice: str, n_play: int, list_size: int) -> None:
    """Play and choose option that will win highest probability of opponent choice."""
    global play_count, result
    
    opp_count: list[str] = []
    

    """Play for n_play number of trials."""
    while play_count < n_play:
        computer_choice: str = computer_play()
        player_choice: str = plyr_choice_eval(p_choice)
        
        """When the list is insufficient, play by RNG."""
        while len(opp_count) < list_size:
            computer_choice: str = computer_play()
            player_choice: str = plyr_choice_eval(p_choice)
            point_eval(player_choice, computer_choice)
            opp_count.append(player_choice)
    
        """Record probability of each option by opponent."""
        rock_prob: int = opp_count.count("Rock") / list_size
        scissor_prob: int = opp_count.count("Scissor") / list_size
        paper_prob: int = opp_count.count("Paper") / list_size
        
        """When the list is sufficient, play according to recent data of list_size."""
        if max(rock_prob, scissor_prob, paper_prob) == rock_prob:
            computer_choice = "Paper"
        elif max(rock_prob, scissor_prob, paper_prob) == scissor_prob:
            computer_choice = "Rock"
        else:
            computer_choice = "Scissor"
        point_eval(player_choice, computer_choice)
        opp_count.append(player_choice)
        opp_count.pop(0)
    
    """Print final results"""
    print(f'The final probability of opponent choosing rock from recent {list_size} trail was: {rock_prob} ')
    print(f'The final probability of opponent choosing paper from recent {list_size} trail was: {paper_prob} ')
    print(f'The final probability of opponent choosing scissor from recent {list_size} trail was: {scissor_prob} ')
    point_check()
    return None


def plyr_choice_eval(p_choice: str) -> str:
    """If p_choice is not RPS, assume player is playing by RNG."""
    player_choice: str = ""
    if p_choice not in {"Rock", "Paper", "Scissor"}:
        player_choice: str = computer_play()
    else:
        player_choice: str = p_choice
    return player_choice


def point_eval(player_choice: str, computer_choice: str) -> None:
    """Evaluate points according to result of a single game."""
    global play_count
    
    if player_choice == "Rock":
        if computer_choice == "Paper":
            result["Paper"] += 1
        elif computer_choice == "Scissor":
            result["Scissor"] -= 1
    elif player_choice == "Paper":
        if computer_choice == "Scissor":
            result["Scissor"] += 1
        elif computer_choice == "Rock":
            result["Rock"] -= 1
    else:
        if computer_choice == "Rock":
            result["Rock"] += 1
        elif computer_choice == "Paper":
            result["Paper"] -= 1
    play_count += 1


def point_check() -> None:
    """Check points after trials."""
    if play_count > 0:
        print(f"The point by rock is {result['Rock']}.")
        print(f"The point by scissor is {result['Scissor']}.")
        print(f"The point by paper is {result['Paper']}.")
        print(f"Total point is {result['Rock'] + result['Paper'] + result['Scissor']}. \n")
        return None


def compare(p_choice: str, trial: int, *sizes: int) -> None:
    """Compare different sizes for same p_choice and trial number."""
    global play_count, result
    
    for size in sizes:
        play_count = 0
        result = {"Rock": 0, "Paper": 0, "Scissor": 0}
        model_prob_based(p_choice, trial, size)


"""RNG Player - list_size 50, 100, 250."""
compare("", 500, 50, 100, 250)


"""Only ROCK Player - list_size 50, 100, 250"""
compare("Rock", 500, 50, 100, 250)