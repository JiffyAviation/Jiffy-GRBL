import ipywidgets as widgets
from IPython.display import display
from control import move_absolute, home, laser_on, laser_off

def build_gui(grbl):
    output = widgets.Output()

    power_slider = widgets.IntSlider(
        value=500, min=0, max=1000, step=10,
        description='Power:', layout=widgets.Layout(width='300px')
    )

    btn_fire = widgets.ToggleButton(
        value=False, description='🔥 FIRE', button_style='danger',
        layout=widgets.Layout(width='100px', height='40px')
    )

    def on_fire_change(change):
        if change['new']:
            laser_on(grbl, power_slider.value)
            with output:
                print(f"🔥 Laser ON at S{power_slider.value}")
        else:
            laser_off(grbl)
            with output:
                print("🛑 Laser OFF")

    btn_fire.observe(on_fire_change, names='value')

    def jog(dx=0, dy=0):
        move_absolute(grbl, x=dx if dx else None, y=dy if dy else None, feed=800)

    btn_up = widgets.Button(description='↑', layout=widgets.Layout(width='40px'))
    btn_down = widgets.Button(description='↓', layout=widgets.Layout(width='40px'))
    btn_left = widgets.Button(description='←', layout=widgets.Layout(width='40px'))
    btn_right = widgets.Button(description='→', layout=widgets.Layout(width='40px'))

    btn_up.on_click(lambda _: jog(dy=10))
    btn_down.on_click(lambda _: jog(dy=-10))
    btn_left.on_click(lambda _: jog(dx=-10))
    btn_right.on_click(lambda _: jog(dx=10))

    jog_grid = widgets.GridBox(
        children=[btn_up, btn_left, btn_right, btn_down],
        layout=widgets.Layout(
            grid_template_columns="40px 40px 40px",
            grid_template_rows="40px 40px",
            grid_gap="5px"
        )
    )

    return widgets.VBox([
        widgets.HBox([power_slider, btn_fire]),
        jog_grid,
        output
    ])
