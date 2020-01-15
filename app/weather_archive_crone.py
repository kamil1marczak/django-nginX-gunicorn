import os
import sqlalchemy as db
from weather_app.weather_api import WeatherApi
from datetime import datetime, timedelta
import sys


class SqlAlchemyScript():
    def __init__(self):
        self.engine = db.create_engine(f'postgresql://{os.getenv("DB_USER", default="postgres")}:{os.getenv("DB_PASSWORD", default="coderslab")}@{os.getenv("HOST_ON_SERVER", default="127.0.0.1")}:{os.getenv("PORT_ON_SERVER", default="54321")}/{os.getenv("DB_NAME", default="weather")}')
        self.connection = self.engine.connect()
        metadata = db.MetaData()
        self.cities_table = db.Table('weather_app_cities', metadata, autoload=True, autoload_with=self.engine)
        self.weather_archive_table = db.Table('weather_app_weatherarchive', metadata, autoload=True, autoload_with=self.engine)

    def find_city(self, city):
        find_city_query = db.select([self.cities_table]).where(self.cities_table.columns.name == city)
        result_proxy = self.connection.execute(find_city_query)
        result_set = result_proxy.fetchone()
        return result_set

    def check_location_city(self, city):
        result_set = self.find_city(city)
        latitude_deg = result_set[2]
        longitude_deg =result_set[3]
        return latitude_deg, longitude_deg

    def find_weather_archive(self, city):
        find_weather_archive_query = db.select([self.weather_archive_table]).where(self.weather_archive_table.columns.city_id == city)
        result_proxy = self.connection.execute(find_weather_archive_query)
        result_set = result_proxy.fetchone
        return result_set


    def insert_weather_data(self, city):
        latitude_deg, longitude_deg = self.check_location_city(city)
        weather_data_context = WeatherApi.weather_json_restructure(latitude_deg, longitude_deg)
        last_update_timestamp = datetime.now() + timedelta(hours=1)
        save_weather_query = db.insert(self.weather_archive_table).values(last_update_timestamp=last_update_timestamp, weather=weather_data_context, city_id=city)
        ResultProxy = self.connection.execute(save_weather_query)
        return ResultProxy

if __name__ == "__main__":
    SqlAlchemyScript().insert_weather_data(sys.argv[1])

