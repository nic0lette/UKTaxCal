"""UK Tax Year Calendar Helper"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
from icalevents.icalevents import events
from icalevents.icalparser import Event
import argparse


def process_events(ical_path: str):
    track_start_date = datetime(2020, 1, 1)
    track_end_date = datetime(2025, 11, 1)

    event_list = events(file=ical_path, fix_apple=True,
                        start=track_start_date, end=track_end_date)
    event_list.sort()

    print("Country visited\tDeparted UK\tArrived UK\tReason for travel (Business / Personal)\tFull days absent")
    for event in event_list:
        if event is None:
            event = Event()
        days = (event.end - event.start).days
        title: str = event.summary
        if title.startswith("Travel"):
            details = title[len("Travel: "):]
            location, extra = details.split(
                "--", 1) if details.find("--") > 0 else (details, "")
            depart = event.start.strftime('%d/%m/%Y')
            arrival = event.end.strftime('%d/%m/%Y')
            reason = "Business" if extra.find("Business") > 0 else "Personal"

            # Because the calendar event includes the day one left and the day one returned
            # the days absent is actually 2 fewer (departure & arrival days don't count)
            full_days_absent = days - 2
            print(
                f"{location}\t{depart}\t{arrival}\t{reason}\t{full_days_absent}")


def main():
    parser = argparse.ArgumentParser(description="Process ical for UK Taxes")
    parser.add_argument("--ical_file", dest="path", required=True)
    args = parser.parse_args()
    process_events(args.path)


if __name__ == '__main__':
    main()
