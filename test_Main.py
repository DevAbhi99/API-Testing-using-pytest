import requests
import pytest


baseUrl='http://localhost:8000'



#Testing get method
@pytest.mark.getTest
def test_getData():
    response=requests.get(f"{baseUrl}/getData")

    assert response.status_code==200

    body=response.json()

    assert body[0]['id']==1
    assert body[0]['name']=='Subhayan'
    assert body[0]['age']==21
    assert body[0]['priority']==1


#Testing post method
@pytest.mark.postTest
def test_sendData():
    payload={'id':2, 'name':'Mohit', 'age':23, 'priority':2}

    response=requests.post(f"{baseUrl}/sendData", json=payload)

    body1=response.json()

    assert body1['message']=='Successfully inserted the data'

    response2=requests.get(f"{baseUrl}/getData")

    assert response2.status_code==200

    body2=response2.json()

    assert body2[1]['id']==2
    assert body2[1]['name']=='Mohit'
    assert body2[1]['age']==23
    assert body2[1]['priority']==2


#testing update method
@pytest.mark.putTest
def test_updateData():

    payload={'id':2, 'name':'Mohit', 'age':23, 'priority':2}

    requests.post(f"{baseUrl}/sendData", json=payload)

    payload2={'id':2, 'name':'Karan', 'age':23, 'priority':2}

    response=requests.put(f"{baseUrl}/updateData/1", json=payload2)

    body=response.json()

    assert body['message']=='Data updated Successfully'

    assert response.status_code==200

    response2=requests.get(f"{baseUrl}/getData")

    body2=response2.json()

    body2[1]['name']=='Karan'


#testing delete method
@pytest.mark.deleteTest
def test_deleteData():

    response=requests.delete(f"{baseUrl}/clearData")

    body=response.json()

    assert response.status_code==200

    assert body['message']=='Data cleared successfully'


    
    


