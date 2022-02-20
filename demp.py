import streamlit as st
import pickle
from PIL import Image

# columns =  [GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
#     CHRONIC_DISEASE, FATIGUE , ALLERGY, WHEEZING, ALCOHOL_CONSUMING,COUGHING, 
#     SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN, LUNG_CANCER]

columns = []

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


def getValue(str):
    if str == "YES" or "Yes" or "yes" or "y":
        return 1
    elif str == "NO" or "No" or "no" or "n":
        return 0
    elif str == "MALE" or "Male" or "male" or "m":
        return 1
    else:
        return 0

def prediction(GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
               CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING,
               SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN):
    predict = model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
                             CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING,
                             SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]]);
#     print(predict)
    return predict



def main():
    
    flag = False;
    
    st.title("Lung Cancer Prediction ")
    st.write(" MALE :: Enter 1  \n   FEMALE :: Enter 0")
#     st.write(" ")
    st.write(" YES :: Enter 1  \n    NO :: Enter 0")
#     st.write("")
    
    GENDER = (st.text_input("GENDER", ""))
    columns.append(getValue(GENDER))

    AGE = int(st.text_input("AGE", "0"))
    columns.append(getValue(AGE))

    SMOKING = int(st.text_input("SMOKING", "0"))
    columns.append(getValue(SMOKING))

    YELLOW_FINGERS = int(st.text_input("YELLOW_FINGERS", "0"))
    columns.append(getValue(YELLOW_FINGERS))

    ANXIETY = int(st.text_input("ANXIETY", "0"))
    columns.append(getValue(ANXIETY))

    PEER_PRESSURE = int(st.text_input("PEER_PRESSURE", "0"))
    columns.append(getValue(PEER_PRESSURE))

    CHRONIC_DISEASE = int(st.text_input("CHRONIC DISEASE", "0"))
    columns.append(getValue(CHRONIC_DISEASE))

    FATIGUE = int(st.text_input("FATIGUE", "0"))
    columns.append(getValue(FATIGUE))

    ALLERGY = int(st.text_input("ALLERGY", "0"))
    columns.append(getValue(ALLERGY))

    WHEEZING = int(st.text_input("WHEEZING", "0"))
    columns.append(getValue(WHEEZING))

    ALCOHOL_CONSUMING = int(st.text_input("ALCOHOL CONSUMING", "0"))
    columns.append(getValue(ALCOHOL_CONSUMING))

    COUGHING = int(st.text_input("COUGHING", "0"))
    columns.append(getValue(COUGHING))

    SHORTNESS_OF_BREATH = int(st.text_input("SHORTNESS OF BREATH", "0"))
    columns.append(getValue(SHORTNESS_OF_BREATH))

    SWALLOWING_DIFFICULTY = int(st.text_input("SWALLOWING DIFFICULTY", "0"))
    columns.append(getValue(SWALLOWING_DIFFICULTY))

    CHEST_PAIN = int(st.text_input("CHEST PAIN", "0"))
    columns.append(getValue(CHEST_PAIN))

    result = ""

    
    if st.button('Predict'):
        result = prediction(GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
                            CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING,
                            SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN)
        flag = True
#     st.success('The Output is {}'.format(result))
    if flag:
        if result == 1:
            st.success("You may have Lung Cancer, Please Contact a Doctor 👨🏼‍⚕️")
        else :
            st.success("You are not showing any signs of Lung Cancer!😀")

    flag = False;

if __name__ == '__main__':
    main()




