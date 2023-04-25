import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]], allot_secondary_y_space=False)
fig1.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=True,
)
fig1.update_layout(title_text="secondary_y=True, allot_secondary_y_space=False")

fig2 = make_subplots(specs=[[{"secondary_y": True}]], allot_secondary_y_space=True)
fig2.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=True,
)
fig2.update_layout(title_text="secondary_y=True, allot_secondary_y_space=True")

fig3 = make_subplots(specs=[[{"secondary_y": False}]], allot_secondary_y_space=False)
fig3.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=False,
)
fig3.update_layout(title_text="secondary_y=False, allot_secondary_y_space=False")

fig4 = make_subplots(specs=[[{"secondary_y": False}]], allot_secondary_y_space=True)
fig4.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=False,
)
fig4.update_layout(title_text="secondary_y=False, allot_secondary_y_space=True")

fig1.show()
fig2.show()
fig3.show()
fig4.show()
