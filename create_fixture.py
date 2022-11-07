from data.csv_to_json import create_fixtures, csv_to_json

if __name__ == '__main__':
    create_fixtures(
        input_file=csv_to_json('data/ads.csv'),
        otput_file='ads/fixtures/ads.json',
        model='ads.ad'
    )

    create_fixtures(
        input_file=csv_to_json('data/categories.csv'),
        output_file='ads/fixtures/categories.json',
        model='categories.ad'
    )
