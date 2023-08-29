class TrelloGTDService:

    def __init__(self, settings):

        self._trello_api = TrelloAPI(settings)

    def add_capture_card(self, card_name, card_description):
        """Add a card to the capture list."""
        organization = self._trello_api.get_organization()
        boards = self._trello_api.get_boards(organization)
        gtd_board = boards['GTD']
        lists = self._trello_api.get_board_lists(gtd_board)
        capture_list = lists['Capture']

        self._trello_api.add_card(
            trello_list=capture_list,
            card_name=name,
            card_desc=description
        )
