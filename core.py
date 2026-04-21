from typing import List, Dict, Any


def calculate_player_stats(player_data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate average stats for a list of players.

    Args:
        player_data (List[Dict[str, Any]]): List of dictionaries containing player stats.

    Returns:
        Dict[str, float]: Dictionary containing average stats.
    """
    total_score = 0
    total_time = 0
    total_players = len(player_data)

    for player in player_data:
        total_score += player.get('score', 0)
        total_time += player.get('time_played', 0)

    avg_score = total_score / total_players if total_players else 0
    avg_time = total_time / total_players if total_players else 0

    return {
        'average_score': avg_score,
        'average_time': avg_time
    }


def log_top_players(player_data: List[Dict[str, Any]], top_n: int = 5) -> None:
    """
    Log the top N players based on their scores.

    Args:
        player_data (List[Dict[str, Any]]): List of dictionaries containing player stats.
        top_n (int): Number of top players to log.
    """
    sorted_players = sorted(player_data, key=lambda x: x.get('score', 0), reverse=True)[:top_n]
    for i, player in enumerate(sorted_players, start=1):
        print(f'#{i} Player: {player.get('name')}, Score: {player.get('score')}')
