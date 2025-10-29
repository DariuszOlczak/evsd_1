import pandas as pd


class Analyzer:
    def __init__(self, df):
        self.df = df
        self.years = [str(year) for year in range(2000, 2024)]

    def get_series_name(self):
        return sorted(self.df['Series Name'].unique().tolist())

    def get_countries(self):
        return sorted(self.df['Country Name'].unique().tolist())

    def get_series_data(self, series_name):
        return self.df[self.df['Series Name'] == series_name]

    def get_country_data(self, country_name):
        return self.df[self.df['Country Name'] == country_name]



    def get_latest_values(self, series, year='2023', n=10):
        data = self.get_series_data(series)
        latest = data[['Country Name', year]].dropna().sort_values(year, ascending=False)
        return latest.head(n)


    def get_trend(self, country, series):
        data = self.get_country_data(country)
        series_data = data[data['Series Name'] == series]
        if series_data.empty:
            return None

        row = series_data.iloc[0]
        trend_data = []
        for year in self.years:
            if year in row and pd.notna(row[year]):
                trend_data.append({
                    'year': year,
                    'value': float(row[year])
                })
        return trend_data

    def summary(self, series, year='2023'):
        data = self.get_series_data(series)
        values = data[year].dropna()
        return {
            'count': len(values),
            'mean': values.mean(),
            'median': values.median(),
            'min': values.min(),
            'max': values.max()
        }
