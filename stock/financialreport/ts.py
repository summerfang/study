from datetime import datetime

date_string = "Nov 19, 2024, 4 PM EST"
format_string = "%b %d, %Y, %I %p %Z"

parsed_datetime = datetime.strptime(date_string, format_string)
print(parsed_datetime)