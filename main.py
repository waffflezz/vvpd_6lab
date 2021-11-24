import re


def main():
    months = {
        '01': '31', '02': '28', '03': '31', '04': '30',
        '05': '31', '06': '30', '07': '31', '08': '31',
        '09': '30', '10': '31', '11': '30', '12': '31',
    }
    dates_list = []

    while len(dates_list) != 2:
        n = input()
        if not re.fullmatch(r'\d\d\.\d\d\.\d{4}', n):
            raise ValueError
        if n[3:5] not in months or int(n[:2]) > int(months[n[3:5]]):
            raise ValueError
        dates_list.append(n)


if __name__ == '__main__':
    main()
