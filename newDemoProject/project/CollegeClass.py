from project.models import College

class CollegeClass:

    #function to fetch college data
    @staticmethod
    def fetch_college_data():
        return College.objects.values()


    #function to update link of a college
    @staticmethod
    def saveUpdatedData(id, link):
        college = College.objects.get('id',id)
        college.link = link
        college.save()