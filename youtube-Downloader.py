from pytube import YouTube
import streamlit as st
print("Youtube Downloader")




# Title of the app
st.title('Youtube Downloader')

# Ask the user for a string input
user_input = st.text_input("Enter URL You need Info Of: ")
submitted = st.button('Submit')

if submitted:
    if not user_input:
        st.error('Error: Input cannot be empty.')
    else:
        # If no errors, display the input string
        try:
            yt = YouTube(user_input)
            st.success("Parsed the URL successfully")
        except Exception as e:
            st.error("Error in parsing URL, please check URL")
            print("Error: ",e)




import requests
import shutil

'''def download_image(url, file_name):
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image successfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
print("Running Image download")
# Call the function
download_image(yt.thumbnail_url, 'download.jpg')'''
