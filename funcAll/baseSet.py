
headers = {  
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/517.56 (KHTML, like Gecko) Chrome/110.0",  
}  

web_url="https://yande.re/post"
pic_url="https://files.yande.re/"

preName=[r'<a class="thumb" href="/post/show/(\d+)" >', 
         r'"sample_url":"(.*?)"', 
         r'id="highres" href="(.*?)"']

picSave="picFile/"
recSave="recFile/"

pageName=["tagCont.html", "postCont.html"]
listName=["picIDs.txt", "picPaths.txt", "picSum.txt"]
timeoutL=[30, 300, 600, 6000]







