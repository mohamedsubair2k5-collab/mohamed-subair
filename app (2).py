import pandas as pd
import streamlit as st

# 2. Load the dataset Book.csv into a pandas DataFrame named df.
df = pd.read_csv('/content/Book.csv')

# 3. Identify numerical and categorical columns in the DataFrame.
# Create two lists: numeric_cols for numerical columns and categorical_cols for categorical columns.
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

# 4. Set the title of the Streamlit application using st.title().
st.title('Book Dataset Interactive Filter App')

# Initialize filtered_df with the original DataFrame
filtered_df = df.copy()

# 5. Create a sidebar using st.sidebar.
st.sidebar.header('Filter Options')

# 6. For each column in numeric_cols, create a slider in the sidebar to filter the data.
# The slider should allow users to select a range (min and max) for each numerical column.
for col in numeric_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    selected_range = st.sidebar.slider(
        f'Select range for {col}',
        min_value=float(min_val),
        max_value=float(max_val),
        value=(float(min_val), float(max_val))
    )
    filtered_df = filtered_df[
        (filtered_df[col] >= selected_range[0]) & (filtered_df[col] <= selected_range[1])
    ]

# 7. For each column in categorical_cols, create a multiselect box in the sidebar to filter the data.
# The multiselect box should display all unique values for each categorical column, and the user can select multiple values.
for col in categorical_cols:
    unique_values = df[col].unique().tolist()
    selected_values = st.sidebar.multiselect(
        f'Select values for {col}',
        options=unique_values,
        default=unique_values
    )
    filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

# 8. Display the filtered_df in the main section of the Streamlit app using st.dataframe().
st.subheader('Filtered Data')
st.dataframe(filtered_df)

st.write("To run this Streamlit app, save the code above as a Python file (e.g., `app.py`) and then execute `streamlit run app.py` in your terminal.")

print("Streamlit app setup complete. Please save the code as a Python file and run it using `streamlit run <filename>.py` to see the interactive filters.")
