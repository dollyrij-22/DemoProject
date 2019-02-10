from project.CollegeClass import CollegeClass
import requests
import csv
from django.http import HttpResponse
from rest_framework.decorators import api_view

#function to check if link is valid or not
@api_view(['GET'])
def link_check(request):
    try:
        #first get all the college data
        colleges = CollegeClass.fetch_college_data()

        #create response with content-type as csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="college.csv"'

        #create a writer for csv
        writer = csv.writer(response)

        #write header for csv
        writer.writerow(['College', 'Link'])

        #for each college check if college link is valid or not if not valid then create generic url and save new url
        for college in colleges:
            #request to check if link is valid
            request = requests.get(college['link'])

            if request.status_code != 200:
                #generate new url
                new_link = create_generic_url(college['name'])

                #update new url
                CollegeClass.saveUpdatedData(college['id'],new_link)

            #for each college put entry in excel
            writer.writerow([college['name'], college['link']])

        return response
    except Exception as e:
        print('Exception % s' % e)

#function to generate generic url
def create_generic_url(name):
    return 'www.'+name+'.com/home'