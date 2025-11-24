def format_date(date_str: str) -> str:
    months = {
        'yanvar': '01',
        'fevral': '02',
        'mart': '03',
        'aprel': '04',
        'may': '05',
        'iyun': '06',
        'iyul': '07',
        'avgust': '08',
        'sentyabr': '09',
        'oktyabr': '10',
        'noyabr': '11', 
        'dekabr': '12',
    }

    day, month, year = date_str.strip().split()
    month = months[month]
    year = year[-2:]
    return f"{day}-{month}-{year}"


print(format_date("24 mart 2025"))
# Output: 24.03.25
