import streamlit as st
import pickle 
import time
import pandas as pd
model = open("rfmodel.pkl", "rb") 
classifier  = pickle.load(model)

def perdicton_price(area_type_no,size,total_sqft,bath, balcony ,price_per_sqft,location_no):
    prediction = classifier.predict([[area_type_no,size,total_sqft,bath, balcony ,price_per_sqft,location_no]])
    return prediction 

def main():
    Prediction, Data_info, Visualization = st.tabs(["Prediction", "Dataset Overview", "Visualization"])

    with Prediction:
        st.title('House Price Prediction')
        st.subheader('Benglore city')
        with st.sidebar:
            # with st.spinner("Loading..."):
            #     time.sleep(5)
            
            st.success("Model Ready!")
            
            st.link_button("Contact Us", "https://www.linkedin.com/in/aakash-mohole-231359233/")
            st.link_button("Contribute", "https://github.com/aakashmohole/ML-Project")

            with st.expander("Devlopers info"):
                st.write("""
                        1. [Aaksh Mohole](https://www.linkedin.com/in/aakash-mohole-231359233/)
                        2. [Vinayak Vathare](https://www.linkedin.com/in/vinayak-vathare-4bb135279/)
                        3. [Shreyash Shetty](https://www.linkedin.com/in/shreyash-shetty-51a640295/)
            
                """)
                #st.image("https://static.streamlit.io/examples/dice.jpg")

        
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

    with Data_info:
        # Add title to the page
        st.title("Data Info page")

        # Add subheader for the section
        st.subheader("View Data")

        # Create an expansion option to check the data
        with st.expander("View Raw data"):
            df = pd.read_csv("D://ML Project//Project 1//src//model//Bengaluru_House_Data.csv")
            st.dataframe(df)
            st.subheader("This Dataset After Preprocessing")
        
        # Create a section to columns values
        # Give subheader
        st.subheader("Columns Description:")

        # Create a checkbox to get the summary.
        if st.checkbox("View Summary"):
            st.dataframe(df.describe().T)

        # Create multiple check box in row
        col_name, col_dtype, col_data = st.columns(3)

        # Show name of all dataframe
        with col_name:
            if st.checkbox("Column Names"):
                st.dataframe(df.columns)

        # Show datatype of all columns 
        with col_dtype:
            if st.checkbox("Columns data types"):
                dtypes = df.dtypes.apply(lambda x: x.name)
                st.dataframe(dtypes)
        
        # Show data for each columns
        with col_data: 
            if st.checkbox("Columns Data"):
                col = st.selectbox("Column Name", list(df.columns))
                st.dataframe(df[col])
                
    with Visualization:
        # Set the page title
        st.title("Visualise Some Demographics")

        # Create a checkbox to show correlation heatmap
        with st.expander("Show the correlation heatmap"):
            st.subheader("Correlation Heatmap")
            st.image("D:\ML Project\Project 1\src\image\corelation.png")
        
        with st.expander("Show prices with features")  : 
            st.subheader("Target Count Relation")
            st.image("D://ML Project//Project 1//src//image//areatype.png")
            
        with st.expander("Show the Outliers"):
            st.subheader("Outliers Detection")
            st.image("D://ML Project//Project 1//src//image//outliers_bath.png")
            st.image("D://ML Project//Project 1//src//image//outliers_sqr.png")
                    
                

if __name__ == '__main__':
    main()