Streamlit is a Python library for building interactive web applications. Below is a list of commonly used Streamlit commands, categorized for easy reference:

---

### **Basic Setup**
- `import streamlit as st`: Import the Streamlit library.
- `st.set_page_config(page_title="Title", layout="wide")`: Configure the page (title, layout, etc.).

---

### **Displaying Text**
- `st.title("Title")`: Display a title.
- `st.header("Header")`: Display a header.
- `st.subheader("Subheader")`: Display a subheader.
- `st.write("Text or variable")`: Write text or render other elements (Markdown, dataframes, etc.).
- `st.markdown("**Markdown Text**")`: Render Markdown content.
- `st.code("Code block", language="python")`: Display a code block.
- `st.caption("Caption text")`: Add a small caption below content.

---

### **Displaying Data**
- `st.dataframe(df)`: Display an interactive dataframe.
- `st.table(data)`: Display static tabular data.
- `st.json(json_data)`: Render JSON data.
- `st.metric(label, value, delta=None)`: Display a KPI-like metric.

---

### **User Inputs**
#### **Text Inputs**
- `st.text_input("Label", value="default text")`: Input a single line of text.
- `st.text_area("Label", value="default text")`: Input multiple lines of text.

#### **Numeric Inputs**
- `st.number_input("Label", value=0, step=1)`: Input a number.

#### **Selections**
- `st.selectbox("Label", options)`: Dropdown menu.
- `st.multiselect("Label", options)`: Select multiple options.
- `st.radio("Label", options)`: Radio buttons.

#### **Sliders**
- `st.slider("Label", min_value, max_value, value)`: Create a slider.
- `st.select_slider("Label", options)`: Slider with specific options.

#### **Buttons**
- `st.button("Label")`: Add a button.
- `st.download_button("Label", data, file_name)`: Create a file download button.

#### **Date/Time Inputs**
- `st.date_input("Label")`: Pick a date.
- `st.time_input("Label")`: Pick a time.

#### **Checkboxes**
- `st.checkbox("Label")`: Add a checkbox.

#### **File Uploader**
- `st.file_uploader("Label", type=["csv", "txt"])`: Upload a file.

---

### **Media**
- `st.image(image, caption=None, use_column_width=False)`: Display an image.
- `st.video(video_path)`: Display a video.
- `st.audio(audio_path)`: Play an audio file.

---

### **Charts and Visualizations**
- `st.line_chart(data)`: Create a line chart.
- `st.bar_chart(data)`: Create a bar chart.
- `st.area_chart(data)`: Create an area chart.
- `st.pyplot(fig)`: Display Matplotlib figures.
- `st.plotly_chart(fig)`: Display Plotly figures.
- `st.altair_chart(chart)`: Display Altair charts.

---

### **Layouts and Containers**
- `st.sidebar`: Access sidebar elements, e.g., `st.sidebar.button("Button in Sidebar")`.
- `st.container()`: Create a container for grouping elements.
- `st.columns(n)`: Split layout into columns, e.g., `col1, col2 = st.columns(2)`.
- `st.expander("Label")`: Add an expandable section.

---

### **Control Flow**
- `st.stop()`: Stop the execution of the app.
- `st.experimental_rerun()`: Rerun the app.

---

### **Session State**
- `st.session_state`: Access and store state variables.
  ```python
  if "key" not in st.session_state:
      st.session_state["key"] = 0
  st.session_state["key"] += 1
  st.write(st.session_state["key"])
  ```

---

### **Other**
- `st.progress(value)`: Add a progress bar.
- `st.spinner("Text")`: Show a spinner while processing.
- `st.toast("Message")`: Show a temporary notification (experimental).
- `st.form("Form Name")`: Create a form for multiple inputs.

---

Let me know if you'd like examples for specific commands!