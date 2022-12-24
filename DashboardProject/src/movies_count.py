import plotly.express as px
import pandas as pd


def fetch_movies(cur, year):
    q = (
        f"SELECT DATE_FORMAT(release_date, '%Y') AS d, COUNT(movie_id) "
        f"FROM movie WHERE DATE_FORMAT(release_date, '%Y') >= {year} GROUP BY d ORDER BY d "
)
    data = []
    try:
        cur.execute(q)
        while True:
            result = cur.fetchone()
            if result:
                data.append(result)
            else:
                break
    except:
        pass
    return [x[1] for x in data], [x[0] for x in data]


def plot_movies(cur, year):
    data = fetch_movies(cur, str(year))
    df = pd.DataFrame({
        'year': data[1],
        'movies': data[0]
    })
    fig = px.bar(df, x='year', y='movies')
    fig.update_layout(
        title={
            'text': (f"Amount of Released Movies by Years"
                     ),
            'y': 0.93,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        })
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    return fig




