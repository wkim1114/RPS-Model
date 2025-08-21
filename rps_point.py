"""Smart RPS machine - Point Based."""


from random import randint


play_count: int = 0
result: dict[str, int] = {"Rock": 0, "Paper": 0, "Scissor": 0}


def computer_play() -> str:
    """Computer choice."""
    rng = randint(0, 2)
    if rng == 0:
        return "Rock"
    if rng == 1:
        return "Paper"
    if rng == 2:
        return "Scissor"


def model_point_based(p_choice: str, n_play: int, RNG_count: int) -> None:
    """Play and choose option with highest point."""
    global play_count
    
    """Play for n_play number of trials."""
    while play_count < n_play:
        """Play by RNG until enough data is collected."""
        if play_count < RNG_count:
            computer_choice: str = computer_play()
        else:
            computer_choice: str = comp_choice_eval()
        player_choice: str = plyr_choice_eval(p_choice)    
        point_eval(player_choice, computer_choice)
    
    """Print final results"""
    point_check()
    return None


def comp_choice_eval() -> str:
    """Computer makes choice according to highest point earned."""
    global result

    computer_choice: str = ""
    if result["Rock"] > result["Paper"] and result["Rock"] > result["Scissor"]:
        computer_choice: str = "Rock"
    elif result["Paper"] > result["Scissor"] and result["Paper"] > result["Rock"]:
        computer_choice: str = "Paper"
    elif result["Scissor"] > result["Rock"] and result["Scissor"] > result["Paper"]:
        computer_choice: str = "Scissor"
    else:
        computer_choice: str = computer_play()
    return computer_choice


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
        model_point_based(p_choice, trial, size)

"""RNG Player - list_size 50, 100, 250."""
compare("", 500, 50, 100, 250)


"""Only ROCK Player - list_size 50, 100, 250"""
compare("Paper", 500, 50, 100, 250)