# UKTaxCal

Tool to help handle date calculations for new arrivals to the UK

## iCal Events

Events are matched by prefixes. For example, "GB Holiday: Spring Bank Holiday" and
"GB Holiday: Boxing Day" are both recognized as bank holidays.

Prefix | Meaning
---|---
GB Holiday: | Bank holiday
PTO | Holiday (Paid Time Off)
Sick | Sick day (Non-working)
Working from | Day working outside the UK
Travel | Days away from the UK

"Travel" events are used to count the number of nights spent outside the UK.
The script expects the start the day you leave (and counts it as the first
"night" sleeping outside the UK), and ends the day _before_ returning,
since you'd be sleeping in the UK that night.

For example: Let's say I were to travel to Ireland for the weekend. I fly
there on April 8th, and return on April 10. I'd be sleeping outside the UK
the night between April 8th to April 9th, and April 9th to April 10th.
I'd be flying back to the UK on the 10th, so I'd be sleeping here then.
The travel event would be an all-day event from April 8th-April 9th.

# Disclaimer

While some amount of care was used to make this software, I am not a tax
expert nor a lawyer in the UK (or anywhere else). Double check the numbers
produced by the software before submitting them to HMRC (or don't blame
me if they ended up being wrong.)