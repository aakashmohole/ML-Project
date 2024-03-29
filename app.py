import streamlit as st
import pickle 
import time
model = open("rfmodel.pkl", "rb") 
classifier  = pickle.load(model)

def perdicton_price(area_type_no,size,total_sqft,bath, balcony ,price_per_sqft,location_no):
    prediction = classifier.predict([[area_type_no,size,total_sqft,bath, balcony ,price_per_sqft,location_no]])
    return prediction 

def main():
    st.title('House Price Prediction')
    st.subheader('Benglore city')
    area_type = st.selectbox(
        'Select Area Type?',
        ('Super built-up  Area', 'Built-up  Area', 'Plot  Area', 'Carpet  Area'))
        
    if(area_type =='Super built-up  Area'):
            area_type_no = 0
    elif(area_type=='Built-up  Area'):
        area_type_no = 1
    elif(area_type=='Built-up  Area'):
        area_type_no = 2
    else: 
        area_type_no = 3
        
    size = st.text_input('Enter BHK Size: ')
    total_sqft = st.text_input('Enter Total Sqrft Size: ')
    bath = st.text_input('Enter No of baths: ')
    balcony	 = st.text_input('Enter Balcony: ')
    price_per_sqft = st.text_input('Enter prcie per Sqrft: ')

    location_mapped =  st.selectbox(
        'Select Location Type?', 
        ('Whitefield',
        'Sarjapur  Road',
        'Electronic City',
        'Kanakpura Road',
        'Thanisandra',
        'Yelahanka',
        'Uttarahalli',
        'Hebbal',
        'Raja Rajeshwari Nagar',
        'Marathahalli',
        'Other'))

    if(location_mapped =='Other'):
            location_no = 0
    elif(location_mapped=='Whitefield'):
        location_no = 1
    elif(location_mapped=='Sarjapur  Road'):
        location_no = 2
    elif(location_mapped=='Electronic City'):
        location_no = 3
    elif(location_mapped=='Kanakpura Road'):
        location_no = 4
    elif(location_mapped=='Thanisandra'):
        location_no = 5
    elif(location_mapped=='Yelahanka'):
        location_no = 6
    elif(location_mapped=='Uttarahalli'):
        location_no = 7
    elif(location_mapped=='Hebbal'):
        location_no = 8
    elif(location_mapped =='Raja Rajeshwari Nagar'):
        location_no = 9
    else: 
        location_no = 10
    result = 0   
    if st.button("Predict"):
            result = perdicton_price(area_type_no,size,total_sqft,bath, balcony ,price_per_sqft,location_no)
    st.success('The Price is {} /- Lacks'.format(result))

if __name__ == '__main__':
    main()