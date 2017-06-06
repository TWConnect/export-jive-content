from utils.fetchUtil import handleListRequest
from models.group import SocialGroup

handleListRequest('https://organization-name.jiveon.com/api/core/v3/places?count=50',
                  SocialGroup.parse_response)
