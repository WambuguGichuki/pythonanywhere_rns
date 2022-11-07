import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from authlib.integrations.requests_client import AssertionSession

# def create_assertion_session(conf_file, scopes, subject=None):
#     with open(conf_file, 'r') as f:
#         conf = json.load(f)

#     token_url = conf['token_uri']
#     issuer = conf['client_email']
#     key = conf['private_key']
#     key_id = conf.get('private_key_id')

#     header = {'alg': 'RS256'}
#     if key_id:
#         header['kid'] = key_id

#     # Google puts scope in payload
#     claims = {'scope': ' '.join(scopes)}
#     return AssertionSession(
#         grant_type=AssertionSession.JWT_BEARER_GRANT_TYPE,
#         token_url=token_url,
#         issuer=issuer,
#         audience=token_url,
#         claims=claims,
#         subject=subject,
#         key=key,
#         header=header,
#     )

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]
# session = create_assertion_session('creds.json', scopes)

# gco = gspread.Client(None,session)

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scopes)
gcs = gspread.authorize(creds)


sh = gcs.open_by_key('1UDav89wEwUjh_7cGDLfCXGRKta9305z6V0hL5R6wzBg')
vh = gcs.open_by_key('1GHFYUCSldTthuZnJxSmMavkxFDvm9fj3XtKM8Qk1qEk')

salessheet = vh.sheet1
expensesheet = sh.sheet1

expense_df = pd.DataFrame(expensesheet.get_all_records())
sales_df = pd.DataFrame(salessheet.get_all_records())


################################################################################


ns = gcs.open_by_key('1kwWsZf06O7KZ7-5DRfUlG3fgntazPlRLWDuPe3Ph-Uo')
ne = gcs.open_by_key('1an68oFHTrv3QTEA3a8GNWPwSyJTtu8cWF7geMryPjpM')
od = gcs.open_by_key('1L_oqESdrtRZwIwWfKQ5E3rIXuBg9BUX-niwyG9PLAxE')

newsalessheet = ns.sheet1
newexpensesheet = ne.sheet1
ordertimesheet = od.sheet1

newsales_df = pd.DataFrame(newsalessheet.get_all_records())
newexpense_df = pd.DataFrame(newexpensesheet.get_all_records())
ordertime_df = pd.DataFrame(ordertimesheet.get_all_records())

# print(newsales_df.columns)
# print(newexpense_df)
# print(ordertime_df)