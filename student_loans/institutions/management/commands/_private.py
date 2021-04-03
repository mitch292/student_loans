from re import L

from student_loans.institutions.models import Institution

SOURCE_ID_COLUMN = 0
NAME_COLUMN = 1
STATE_COLUM = 2
ZIP_COLUM = 3
TYPE_COLUM = 4
DL_SUB_RECEPIENTS_COLUMN = 5
DL_SUB_ORIGINATED_COUNT_COLUMN = 6
DL_SUB_ORIGINATED_AMOUNT_COLUMN = 7
DL_SUB_DISBURSEMENTS_COUNT_COLUMN = 8
DL_SUB_DISBURSEMENTS_AMOUNT_COLUMN = 9
DL_UNSUB_UNDER_RECEPIENTS_COLUMN = 10
DL_UNSUB_UNDER_ORIGINATED_COUNT_COLUMN = 11
DL_UNSUB_UNDER_ORIGINATED_AMOUNT_COLUMN = 12
DL_UNSUB_UNDER_DISBURSEMENTS_COUNT_COLUMN = 13
DL_UNSUB_UNDER_DISBURSEMENTS_AMOUNT_COLUMN = 14
DL_UNSUB_GRAD_RECEPIENTS_COLUMN = 15
DL_UNSUB_GRAD_ORIGINATED_COUNT_COLUMN = 16
DL_UNSUB_GRAD_ORIGINATED_AMOUNT_COLUMN = 17
DL_UNSUB_GRAD_DISBURSEMENTS_COUNT_COLUMN = 18
DL_UNSUB_GRAD_DISBURSEMENTS_AMOUNT_COLUMN = 19
DL_PARENT_PLUS_RECEPIENTS_COLUMN = 20
DL_PARENT_PLUS_ORIGINATED_COUNT_COLUMN = 21
DL_PARENT_PLUS_ORIGINATED_AMOUNT_COLUMN = 22
DL_PARENT_PLUS_DISBURSEMENTS_COUNT_COLUMN = 23
DL_PARENT_PLUS_DISBURSEMENTS_AMOUNT_COLUMN = 24
DL_GRAD_PLUS_RECEPIENTS_COLUMN = 25
DL_GRAD_PLUS_ORIGINATED_COUNT_COLUMN = 26
DL_GRAD_PLUS_ORIGINATED_AMOUNT_COLUMN = 27
DL_GRAD_PLUS_DISBURSEMENTS_COUNT_COLUMN = 28
DL_GRAD_PLUS_DISBURSEMENTS_AMOUNT_COLUMN = 29


def map_fsa_str_to_type(name: str) -> str:
    if name == "Public":
        return Institution.Type.PUBLIC
    if name == "Private-Nonprofit":
        return Institution.Type.PRIVATE_NONPROFIT
    if name == "Proprietary":
        return Institution.Type.PROPRIETARY
    if name == "Foreign-Private":
        return Institution.Type.FOREIGN_PRIVATE
    if name == "Foregin-Public":
        return Institution.Type.FOREIGN_PUBLIC
    if name == "Foreign-For-Profit":
        return Institution.Type.FOREIGN_FOR_PROFIT
    return Institution.Type.UNKOWN