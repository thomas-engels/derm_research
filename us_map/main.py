import pandas as pd
import turtle

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.addshape(IMAGE)
turtle.shape(IMAGE)

df_50_states = pd.read_csv('50_states.csv')
df_derm_access = pd.read_csv('derm_access_by_state.csv')

df_50_states.sort_values('abbreviation', inplace=True, ignore_index=True)
df_derm_access.sort_values('Rndrng_Prvdr_State_Abrvtn', inplace=True, ignore_index=True)
df_derm_access['derm_access_score'] = df_derm_access['derm_access_score'].round(decimals=2)
print(df_derm_access['derm_access_score'])

state_coordinates = []
for row, index in df_50_states.iterrows():
    state_coordinates.append((index['x'], index['y']))

counter = 0
for row, index in df_derm_access.iterrows():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    x_cor = int(state_coordinates[counter][0])
    y_cor = int(state_coordinates[counter][1])
    t.goto(x_cor, y_cor)
    t.write(f"{index['Rndrng_Prvdr_State_Abrvtn']}\n {index['derm_access_score']}")
    counter += 1

while True:
    turtle.mainloop()


