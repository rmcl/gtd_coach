from typing import List
from langchain.agents import tool
from trello_utils.service import get_trello_gtd_service


@tool
def get_recently_closed_cards(when : str = 'today') -> List[str]:
    """Get recently closed cards from the GTD next action"""

    trello_list_name = 'Next Action'

    gtd_service = get_trello_gtd_service()
    closed_cards = gtd_service.get_closed_cards(
        trello_list_name,
        when=when)

    if not closed_cards:
        return 'No recently closed cards.'

    return '\n'.join([
        f'{card.name} - {card.desc}'
        for card in closed_cards
    ])

@tool
def capture_and_create_new_card(description: str) -> bool:
    """Capture and create a card in the GTD capture list."""
    gtd_service = get_trello_gtd_service()
    gtd_service.add_capture_card(description, '')
    return True

@tool
def get_next_action_cards(count : int = 3) -> List[str]:
    """Get next action cards from the GTD next action list. Count is the number of cards to return defaults to 3."""
    gtd_service = get_trello_gtd_service()

    next_action_cards = gtd_service.get_next_action_cards(count)
    return '\n'.join([
        f'{card.name} - {card.desc}'
        for card in next_action_cards
    ])

GTD_TOOLS = [
    get_recently_closed_cards,
    get_next_action_cards,
    capture_and_create_new_card
]
