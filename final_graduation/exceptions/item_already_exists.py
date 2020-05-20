from final_graduation.kernal import AppException


class ItemAlreadyExists(AppException):
    def __init__(self, item_name: str):
        super().__init__(f'{item_name} already exists.')
