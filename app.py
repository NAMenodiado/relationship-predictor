import streamlit as st
import pandas as pd
import numpy as np # Used for dummy prediction and slider default value
from transform import manual_one_hot_encode
import pickle

# --- Dummy Prediction Function ---
# IMPORTANT: Replace this with your actual model loading and prediction logic
def predict_relationship_duration(input_df):
    try:

        with open('rf_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        
        prediction = loaded_model.predict(input_df)
        final_prediction = prediction[0]
        final_prediction = round(final_prediction)
        # prediction = round(prediction)

        return final_prediction

    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return "Prediction Error"
    # -----------------------------------------------------------


st.set_page_config(page_title="Relationship Duration Prediction", layout="centered")

st.title("Relationship Questionnaire")
st.markdown("Please answer the following questions to get a prediction on relationship duration.")
st.markdown("Note: This is for demonstration purposes only! Model is not accurate due to low volume of data gathered.")
st.markdown("We are not liable in any way for any problems in your relationship!")


# Load the original data to get column names and unique values for options
try:
    df_questions = pd.read_csv('complete_responses.csv')  ### Change this
    # Exclude the target column from questions to be asked
    target_column = "How many months did you and your other half last? (If you're still together, how many months has it been?)"
    feature_columns = [col for col in df_questions.columns if col != target_column]
except FileNotFoundError:
    st.error("`sample_responses.csv` not found. Please ensure it's in the same directory.")
    st.stop() # Stop the app if the file is not found

# Dictionary to store user inputs
user_answers = {}

st.markdown("---")
st.header("Your Profile")

# Group questions for better UI based on the common structure from your data
your_questions = [
    "Do you enjoy the outdoors more or indoors?",
    "Would you say that you are more the \"artistic\" type or the \"sporty\" type?",
    "Do you enjoy going out more or having more \"me\" or \"alone\" time?",
    "Do you enjoy cooking? (For yourself or even for others?)",
    "Are you someone who currently wants to have a long term relationship or nah? ",
    "Do you want to have children in the future? ",
    "Do you value career more or family?",
    "Do you smoke?",
    "Do you drink? (Like really enjoy it)",
    "Do you prefer staying up late at night? Or do you prefer waking up early in the morning?",
    "Do you like pets?",
    "Do you avoid conflict or confronts issues?",
    "Do you express your emotions openly or in private?",
    "How open are you to trying new things? "
]

for i, question in enumerate(your_questions):
    if question in feature_columns:
        st.subheader(f"Question {i+1}")
        if df_questions[question].dtype == 'object':
            options = df_questions[question].dropna().unique().tolist()
            user_answers[question] = st.radio(question, options, key=f"q_your_{i}")
        elif df_questions[question].dtype == 'int64':
            # min_val = df_questions[question].min()
            # max_val = df_questions[question].max()
            min_val = 1
            max_val = 10
            # Set a sensible default value, e.g., the mean or midpoint
            default_val = int(df_questions[question].mean()) if not pd.isna(df_questions[question].mean()) else 5
            user_answers[question] = st.slider(question, min_value=min_val, max_value=max_val, value=default_val, key=f"q_your_{i}")

st.markdown("---")
st.header("Your Partner's Profile")

partner_questions = [
    "[PARTNER] Does he/she/they enjoy the outdoors more or indoors?",
    "[PARTNER]  Does he/she/they enjoy going out more or having more \"me\" or \"alone\" time?",
    "[PARTNER] Does he/she/they enjoy cooking?",
    "[PARTNER]  Is he/she/they someone who currently wants to have a long term relationship or nah? ",
    "[PARTNER]  Does he/she/they want to have children in the future? ",
    "[PARTNER] Does he/she/they value career more or family?",
    "[PARTNER] Does he/she/they smoke?",
    "[PARTNER] Does he/she/they drink?  (Like really enjoy it)",
    "[PARTNER] Does he/she/they prefer staying up late at night? Or do you prefer waking up early in the morning?",
    "[PARTNER] Does he/she/they like pets?",
    "[PARTNER] Would you say that he/she/they is more the \"artistic\" type or the \"sporty\" type?",
    "[PARTNER] Does he/she/they avoid conflict or confronts issues?",
    "[PARTNER] Does he/she/they express his/her/their emotions openly or in private?",
    "[PARTNER] How open is he/she/they to trying new things? "
]

for i, question in enumerate(partner_questions):
    if question in feature_columns:
        st.subheader(f"Question {i+1} (Partner)")
        if df_questions[question].dtype == 'object':
            options = df_questions[question].dropna().unique().tolist()
            user_answers[question] = st.radio(question, options, key=f"q_partner_{i}")
        elif df_questions[question].dtype == 'int64':
            # min_val = df_questions[question].min()
            # max_val = df_questions[question].max()
            min_val = 1
            max_val = 10
            default_val = int(df_questions[question].mean()) if not pd.isna(df_questions[question].mean()) else 5
            user_answers[question] = st.slider(question, min_value=min_val, max_value=max_val, value=default_val, key=f"q_partner_{i}")

st.markdown("---")
st.header("Relationship Status")

# relationship_status_question = "Is the other person an ex or a current somebody?"
# if relationship_status_question in feature_columns:
#     options = df_questions[relationship_status_question].dropna().unique().tolist()
#     user_answers[relationship_status_question] = st.radio(relationship_status_question, options, key="q_relationship_status")

relationship_status_question = "Is the other person an ex or a current somebody?"
options = ['Not Yet', 'Currently Together']
user_answers['Is this someone you are currently with or not yet?'] = st.radio("Is this someone you are currently with or not yet?", options, key="q_relationship_status")

st.markdown("---")
st.header("Prediction Result")

# Button to trigger prediction
if st.button("Get Relationship Duration Prediction"):
    if user_answers:
        # Create a DataFrame from the collected user answers
        # This ensures the DataFrame has the correct column names for your model
        user_responses_df = pd.DataFrame([user_answers])

        user_responses_df = manual_one_hot_encode(user_responses_df)
        print(user_responses_df)
        
        st.subheader("Your Predicted Relationship Duration (in months):")
        
        # Call the prediction function with the collected answers DataFrame
        prediction_result = predict_relationship_duration(user_responses_df)
        
        if prediction_result:
            st.success(f"**Prediction:** {prediction_result}")
            st.markdown("---")
            st.write("### Data sent to the Model for Prediction:")
            st.dataframe(user_responses_df)
        else:
            st.warning("Could not generate a prediction. Please answer all questions.")
    else:
        st.warning("Please answer the questions before getting a prediction.")
