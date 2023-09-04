from datetime import date, timedelta
from trello_utils.trello_api import TrelloAPI
from django.conf import settings

class TrelloGTDService:
    """Service for interacting with Trello for GTD."""

    def __init__(self, settings):
        self._trello_api = TrelloAPI(settings)

    def add_capture_card(self, card_name : str, card_description : str):
        """Add a card to the capture list."""
        organization = self._trello_api.get_organization()
        boards = self._trello_api.get_boards(organization)
        gtd_board = boards['GTD']
        lists = self._trello_api.get_board_lists(gtd_board)
        capture_list = lists['Capture']

        self._trello_api.add_card(
            trello_list=capture_list,
            card_name=card_name,
            card_description=card_description
        )

    def get_closed_cards(self, list_name : str, when : str = 'today'):
        """Get closed cards from a list."""
        organization = self._trello_api.get_organization()
        boards = self._trello_api.get_boards(organization)
        gtd_board = boards['GTD']
        trello_lists = self._trello_api.get_board_lists(gtd_board)

        if when == 'today':
            card_date = date.today()
        elif when == 'yesterday':
            card_date = date.today() - timedelta(days=1)

        return self._trello_api.get_closed_cards(
            trello_lists[list_name],
            card_date)

    def get_next_action_cards(self, count : int):
        organization = self._trello_api.get_organization()
        boards = self._trello_api.get_boards(organization)
        gtd_board = boards['GTD']
        trello_lists = self._trello_api.get_board_lists(gtd_board)

        return self._trello_api.get_cards(trello_lists['Next Action'], count=count)

def get_trello_gtd_service():
    """Get the Trello GTD service."""
    return TrelloGTDService(settings.GTD_COACH)
