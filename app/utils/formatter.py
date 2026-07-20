from datetime import datetime

import jdatetime


def to_jalali_date(value):

    if not value:
        return "-"

    try:

        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        gregorian_date = value.date() if hasattr(value, "date") else value

        jalali = jdatetime.date.fromgregorian(date=gregorian_date)

        digits = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

        return jalali.strftime("%Y/%m/%d").translate(digits)

    except Exception:
        return "-"
    
    
def format_price(service):

    minimum_price = service.get("minimum_price")
    maximum_price = service.get("maximum_price")

    if not minimum_price:
        return "تماس بگیرید"

    if maximum_price and maximum_price > minimum_price:
        return f"{minimum_price:,} تا {maximum_price:,} تومان"

    return f"{minimum_price:,} تومان"