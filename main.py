"""UK Tax Year Calendar Helper"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from icalevents.icalevents import events
from icalevents.icalparser import Event
import argparse


def process_events(ical_path: str):
    tax_year_start = datetime(2021, 4, 6)
    tax_year_end = tax_year_start + relativedelta(years=1)
    total_days_in_year = 365
    total_working_days = 255

    event_list = events(file=ical_path, fix_apple=True, start=tax_year_start, end=tax_year_end)
    event_list.sort()
    print(f"Found {len(event_list)} events")

    bank_holidays = 0
    sick_days = 0
    special_holidays = 0
    foreign_workdays = 0
    nights_outside_uk = 0
    personal_holiday = 0

    for event in event_list:
        if event is None:
            event = Event()
        days = (event.end - event.start).days
        if event.summary.startswith("Travel"):
            nights_outside_uk += days

        if event.summary.startswith("GB Holiday:"):
            bank_holidays += days
        if event.summary.startswith("PTO"):
            personal_holiday += days
        if event.summary.startswith("Sick"):
            sick_days += days
        if event.summary.startswith("Google"):
            special_holidays += days
        if event.summary.startswith("Working from"):
            foreign_workdays += days

    non_working_days = personal_holiday + sick_days + special_holidays

    print(f"UK bank holidays: {bank_holidays}")
    print(f"Sick days: {sick_days}")
    print(f"Special Leave Days: {special_holidays}")
    print(f"Foreign Workdays: {foreign_workdays}")
    print(f"Nights sleeping outside the UK: {nights_outside_uk}")
    print(f"----------------------------------------------------")
    print(f"Nights in the UK: {total_days_in_year - nights_outside_uk}")
    print(f"Days worked in UK: {total_working_days - non_working_days}")


def main():
    parser = argparse.ArgumentParser(description="Process ical for UK Taxes")
    parser.add_argument("--ical_file", dest="path", required=True)
    args = parser.parse_args()
    process_events(args.path)


if __name__ == '__main__':
    main()
