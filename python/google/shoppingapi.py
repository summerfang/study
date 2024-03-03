import pprint

from googleapiclient.discovery import build


SHOPPING_API_VERSION = "v1"
DEVELOPER_KEY = "AIzaSyA4-JAgc1wPvuCuXwlfhlLrP0TxqF8HebQ"


def main():
    """Get and print a feed of all public products available in the
    United States.

    Note: The source and country arguments are required to pass to the list
    method.
    """
    client = build("shopping", SHOPPING_API_VERSION, developerKey=DEVELOPER_KEY)
    resource = client.products()
    resource = client.products()
    request = resource.list(source="public", country="US")
    response = request.execute()
    pprint.pprint(response)


if __name__ == "__main__":
    main()