import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title("🎨 Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("🔍 Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")
import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Load color dataset
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv", names=["color", "color_name", "hex", "R", "G", "B"], header=None)

colors = load_colors()

# Find closest color name
def get_color_name(R, G, B):
    min_dist = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, "R"])) + abs(G - int(colors.loc[i, "G"])) + abs(B - int(colors.loc[i, "B"]))
        if d < min_dist:
            min_dist = d
            cname = colors.loc[i, "color_name"]
    return cname

st.title(" Color Detection from Image")
st.write("Upload an image, click to detect the color, and view its RGB and closest name.")

uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Get click position
    click = st.experimental_data_editor(image_np, key="click_editor", disabled=True)

    st.write("Click on the image to detect a color.")

    if 'click' in st.session_state:
        if st.session_state.click:
            x = st.session_state.click['row']
            y = st.session_state.click['column']
            try:
                b, g, r = image_bgr[x, y]
                color_name = get_color_name(r, g, b)
                st.markdown(f"**Detected Color:** {color_name}")
                st.markdown(f"**RGB:** ({r}, {g}, {b})")
                st.markdown(
                    f"<div style='width:100px;height:100px;background-color:rgb({r},{g},{b});'></div>",
                    unsafe_allow_html=True
                )
            except:
                st.warning("Click within the image boundaries.")