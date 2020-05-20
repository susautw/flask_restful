from final_graduation.kernal import AppException


class NoDataFound(AppException):
    def __init__(self, query: str):
        """
        :param query: A string describes the query' content.
        """
        super().__init__(f'no data found in this query: {query}')
