from typing import Optional, Dict, List
from datetime import date, timedelta
from trello import TrelloClient, Card

class TrelloAPI:

    def __init__(self, settings):

        self._org_display_name = settings.get('org_display_name', 'Russell GTD')

        trello_api_key = settings.get('TRELLO_API_KEY', None)
        trello_api_secret = settings.get('TRELLO_API_SECRET', None)
        trello_api_token = settings.get('TRELLO_API_TOKEN', None)

        if not trello_api_key or not trello_api_secret or not trello_api_token:
            raise Exception('TRELLO_API_KEY, TRELLO_API_SECRET, or TRELLO_API_TOKEN not found in settings')

        self._client = TrelloClient(
            api_key=trello_api_key,
            api_secret=trello_api_secret,
            token=trello_api_token
        )

    def get_organization(self):
        orgs = self._client.list_organizations()

        for org in orgs:
            if org.displayName == self._org_display_name:
                return org

        return None

    def get_boards(self, trello_organization):
        boards = trello_organization.get_boards('*')
        return {
            board.name: board
            for board in boards
        }

    def get_board_lists(self, board) -> Dict[str, List[Card]]:
        return {
            trel_list.name: trel_list
            for trel_list in board.all_lists()
            if not trel_list.closed
        }

    def add_card(self, trello_list, card_name, card_description):
        """Add a card to the capture list."""
        organization = self.get_organization()
        boards = self.get_boards(organization)
        gtd_board = boards['GTD']
        lists = self.get_board_lists(gtd_board)
        capture_list = lists['Capture']

        return capture_list.add_card(name=card_name, desc=card_description)


    def get_cards(self, trello_list, count : Optional[int] = None):
        """Get cards from a list."""
        organization = self.get_organization()
        cards = trello_list.list_cards()

        if count is None:
            return cards
        return cards[0:count]

    def get_closed_cards(self, trello_list, closed_date : Optional[date] = None):
        """Get closed cards from a list."""
        organization = self.get_organization()

        closed_cards = trello_list.list_cards(
            card_filter='closed')

        if closed_date:
            closed_cards_on_date = [
                closed_card
                for closed_card in closed_cards
                if  closed_card.date_last_activity.date() == closed_date
            ]

            return closed_cards_on_date

        return closed_cards
