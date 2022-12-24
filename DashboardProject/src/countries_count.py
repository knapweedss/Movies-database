import plotly.express as px
import pandas as pd


def fetch_countries(cur, n_country):
    q = (
        f"SELECT country AS d, COUNT(country) "
        f"FROM companie GROUP BY country LIMIT {n_country} "
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


def plot_countries(cur, n_country):
    data = fetch_countries(cur, str(n_country))
    df = pd.DataFrame({
        'value': data[1],
        'country': data[0]
    })
    fig = px.bar(df, x='country', y='value')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    return fig
