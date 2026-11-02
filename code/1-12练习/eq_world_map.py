import plotly.express as px

fig = px.scatter(
    x=lons,
    y=lats,
    labels={'x': "经度", 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
)
fig.write_html('goibal_earthquakes.html')
fig.show

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
)
fig.write_himl('global_earthquakes.html')
fig.show()