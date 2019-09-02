from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "https://map.hackney.gov.uk/geoserver/wms?SERVICE=WFS&VERSION=1.3.0&request=GetFeature&typeNames=government%3Apolling_station&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'E09000012'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
