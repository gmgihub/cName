# cName
Only for changing file's name with SAME SEQUENCE name that stored in .txt file
***
Using '-h' option for little help:

```
python cName.py -h

  BRIEF
         It can change specify type file's name in path into new name stored in .txt

  MAKESURE
	.txt file is UTF-8(without BOM)

  USAGE
	python cName.py  .txt  path  *.xxx
```
## Example
I have 3 .docx files: '1.docx'、'2.docx'、'3.docx' and they are sorted by name.

Now i want to change their name: 

	1.docx -> A.docx  

	2.docx -> B.docx  

	3.docx -> C.docx

 
   ![alt text](https://github.com/gmgihub/cName/blob/main/pic/Screenshot%202023-11-14%20214512.jpg) 
   
  
So i create a .txt file and fill 'A' 'B' 'C' in sequence.

 
   ![alt text](https://github.com/gmgihub/cName/blob/main/pic/txt_store.jpg) 
   

Then run the python script and we can change their name.

 
   ![alt text](https://github.com/gmgihub/cName/blob/main/pic/Screenshot%202023-11-14%20215543.jpg) 


## Bug
So,if you are a cautious person, you will find out this script can't replace .txt type file's name cause our new name is stored in .txt file.And for this reason, i recommend you use a suffixless file to store new name.Hope this can work!

![bug](https://github.com/gmgihub/cName/blob/main/pic/bug.jpg)

