from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form-api.html')


@app.route('/', methods=['POST'])
def my_form_post():
    api = request.form['api']
    api1=api.split()
    api_len=len(api1)

    pt = request.form['pt']
    pt1=pt.split()
    pt_len=len(pt1)

    link= request.form['link']
    link1=link.split()
    link_len=len(link1)

    processing_link=[]
    
    res=""
    link_temp=""
    #j='\\",\\"'
    j="\",\""

    un_processing_link_numb=0
    un_processing_link=[]
    
    links199=[]
    link_temp199=[]
        
    temp_count = 0
    #temp_count_1=""
    max_link = api_len*199                                                      # MAXIMUM LINKS 
    
    if api_len == pt_len:
        if link_len > max_link:
            ip_link=199
            #return str(ip_link)+'if'
        else:
            ip_link = link_len/api_len
            #return str(ip_link)+'else'                                                  # MAXIMUM LINKS SHARE ON EACH API
    
        temp_count_max = int(ip_link)    
        temp_count_max_1 = int(ip_link)
        #remaining_links= link_len-(api_len*int(ip_link))

        if link_len > max_link:
            z=0
            for n in range(0,max_link):
                processing_link.append(link1[n])
                un_processing_link_numb=max_link-link_len
            for n in range(max_link-un_processing_link_numb,link_len):
                un_processing_link[z]=un_processing_link.append(link1[z])
                z=z+1
        else:
            for n in range(0,link_len):
                processing_link.append(link1[n])
        for ii in range(0,api_len):#temp_count_max-1):
			#temp_count_1= temp_count_1+"<br> Set "+str(ii)
            for i in range(temp_count,temp_count_max_1):
				#temp_count_1=temp_count_1+'<br>'+str(i)
                link_temp199.append(processing_link[i])
            temp_count=i+1
            temp_count_max_1=temp_count_max_1+temp_count_max
            #return str(link1[0])+'<br>'+str(link1[1])
            link_temp=j.join(link_temp199)
            #return 'link_temp'
            #links199.append('[\\"'+link_temp+'\\"]')
            #links199.append('{\\"url\\":[\\"'+link_temp+'\\"]}')
            #links199.append('"{\\"url\\":[\\"'+link_temp+'\\"]}"')
            links199.append("{\"url\":[\""+link_temp+"\"]}")
            #return 'append over'
            params = {
                    "api_key": api1[ii],
                    "start_url": "https://www.amazon.in/","start_template": "main_template",
                    "start_value_override": links199[ii],
                    "send_email": "1"
                    }
            r = requests.post("https://www.parsehub.com/api/v2/projects/"+pt1[ii]+"/run", data=params)
            res = res +' <br> '+ r.text
            link_temp199=[]
            time.sleep(5)
    
		#temp_count_1
        res="Successfully Completed 5 Projects"+'<br><br>'+ res
        for nn in range(0,un_processing_link_numb):
            res = res + '<br>' + un_processing_link[nn]
        res="Un Processed Links Due to Over Load <br>" + res
		
        return res#+temp_count_1+'<br><br>'+str(remaining_links)
    
    else:
        er="Please provide same number of API_KEY and PROJECT_TOKEN"
        return er



if __name__ == '__main__':
    app.run()    
