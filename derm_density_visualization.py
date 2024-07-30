import pandas as pd
import plotly.express as px

df_derm_providers_by_zip = pd.read_csv('/data/derm_providers_by_zip.csv')

df_state_view = df_derm_providers_by_zip.groupby('Rndrng_Prvdr_State_Abrvtn').agg({
    'irs_estimated_population': pd.Series.sum,
    'derm_provider_count': pd.Series.sum,
}).reset_index()

df_state_view['derm_access_score'] = (df_state_view['derm_provider_count']
                                       .div(df_state_view['irs_estimated_population']))*10000
# df_state_view.sort_values('derm_access_score', ascending=False, inplace=True)

# bar_graph = px.bar(
#     x=df_state_view['Rndrng_Prvdr_State_Abrvtn'],
#     y=df_state_view['derm_access_score']
# )
#
# bar_graph.show()

df_state_view.sort_values('derm_access_score', ascending=False, inplace=True)

df_state_view.to_csv('/data/derm_access_by_state.csv', index=False, encoding='utf-8', header=True)
print(df_state_view.to_string())


sort_bar_graph = px.bar(
    x=df_state_view['Rndrng_Prvdr_State_Abrvtn'],
    y=df_state_view['derm_access_score']
)

sort_bar_graph.update_layout(
    title={
        'text': 'Dermatology Access Scores by State',
        'x':0.5,  # Centers the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='US States and Territories',
    yaxis_title='Dermatology Access Score')

# sort_bar_graph.update_layout(yaxis=dict(type='log'))

sort_bar_graph.show()

# color_scale=['#e60b13', '#f58814', '#23eb48']
# fig = px.scatter(df_state_view.head(25),
#                  x="Rndrng_Prvdr_State_Abrvtn",
#                  y="irs_estimated_population",
#                  # size="derm_access_score",
#                  size=[10] * len(df_state_view.head(25)),  #
#                  color="derm_access_score",
#                  hover_name=df_state_view.index[:25],
#                  title='Population vs Dermatology Access',
#                  labels={'Rndrng_Prvdr_State_Abrvtn': 'State', 'irs_estimated_population': 'Population', 'derm_access_score': 'Dermatology Access Score'},
#                  color_continuous_scale=color_scale)
#
# # fig.update_layout(yaxis=dict(type='log'))
# fig.show()

