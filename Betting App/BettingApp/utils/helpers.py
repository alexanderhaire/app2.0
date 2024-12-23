FIXED_PLATFORM_RAKE = 0.05

def calculate_odds(bets, user_rake=0, platform_rake=FIXED_PLATFORM_RAKE):
    total_rake = user_rake + platform_rake
    total_pool = sum(bets.values())
    pool_after_rake = total_pool * (1 - total_rake)

    odds = {}
    for participant, bet_amount in bets.items():
        if bet_amount > 0:
            payout_pool = pool_after_rake
            odds[participant] = (payout_pool / bet_amount) - 1
        else:
            odds[participant] = float('inf')

    formatted_odds = {
        k: f"{v:.2f}x" if v != float('inf') else "No Bets"
        for k, v in odds.items()
    }
    return formatted_odds
