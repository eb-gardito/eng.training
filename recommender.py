import csv
import statistics  # see https://docs.python.org/3/library/statistics.html
import sys

CATEGORY_MAP = {
    'Sports': '101',
}
PRICES_SOURCE_FILE = 'src/ebengtraining.csv'


def get_prediction(country_code, event_category):
    """
    Returns the mean and standard deviation for purchases for the provided country and event category.
    :Parameters:
        - `country_code` (str)
        - `event_category` (str): Human-friendly alias for a Category ID.
    :Returns:
    Dictionary with 'mean' and 'standard_deviation' as keys and floats as values.
    """
    event_category_id = CATEGORY_MAP.get(event_category)

    filtered_prices = get_prices_by_filter(country_code, category_id=event_category_id)

    mean = statistics.mean(filtered_prices)

    return {
        'mean': mean,
        'standard_deviation': statistics.stdev(filtered_prices, mean),
    }


def get_prices_by_filter(country_code, category_id):
    # get prices from source
    # "currency","id","country","category_id","price_ticket_amount","purchased_at","quantity_sold"

    prices = []
    with open(PRICES_SOURCE_FILE, newline='') as csvfile:
        rows = csv.DictReader(csvfile, delimiter=',')
        for row in rows:
            if row.get('country') == country_code and row.get('category_id') == category_id:
                prices.append(
                    float(row.get('price_ticket_amount')) * int(row.get('quantity_sold'))
                )

    return prices


#  it happen only when command is ran from console
if __name__ == '__main__':
    country_code, category = sys.argv[1:3]
    print(
        get_prediction(country_code, category)
    )
