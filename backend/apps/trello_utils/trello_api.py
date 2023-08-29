from trello import TrelloClient

class TrelloAPI:

    def __init__(self, settings):

        self._org_display_name = settings.get('org_display_name', 'Russell GTD')

        self._client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TRELLO_API_TOKEN
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

    def get_board_lists(self, board):
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
