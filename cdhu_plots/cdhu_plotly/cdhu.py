import plotly.graph_objects as go
import plotly.io as pio

cdhu_layout = {
    # Fonts
    # Note - 'family' must be a single string, NOT a list or dict!
    "title": {
        "font": {
            "family": "Lato",
            "size": 30,
            "color": "#333",
        }
    },
    "font": {
        "family": "Lato",
        "size": 16,
        "color": "#333",
    },
    # Colorways
    "colorway": [
        "#000000",
        "#4e210d",
        "#c0281b",
        "#ea33d2",
        "#a53df6",
        "#dcaf3b",
        "#55baac",
        "#51b3f9",
    ]
    # Keep adding others as needed below
}

pio.templates["cdhu"] = go.layout.Template(layout=cdhu_layout)
