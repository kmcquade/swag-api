from flask_restplus import reqparse, Resource

from swag_api.api import api
from swag_api.extensions import swag
from swag_api.common.swag import get_account
from swag_api.parsers import namespace_arguments


@api.route('/<namespace>')
class NameSpace(Resource):

    @api.expect(namespace_arguments)
    @api.response(200, 'List of all accounts')
    def get(self, namespace):
        """
        Returns all accounts in the namespace.
        Example: For a namespace `accounts`, a list of accounts will be returned based on [Account Schema](https://github.com/Netflix-Skunkworks/swag-client/blob/master/swag_client/schemas/v2.py#L43)
        """
        swag.namespace = namespace
        return swag.get_all()