import requests
import datetime as dt

# TODO-1 Create a Pixela account.
username = "rastog18"
password = "bdbdbqeh23100"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameter = {"token": "bdbdbqeh23100",
                    "username": "rastog18",
                    "agreeTermsOfService": "yes",
                    "notMinor": "yes"}
# response = requests.post(url=pixela_endpoint,json=pixela_parameter)
# response.raise_for_status()

# TODO-2 Create a Pixela Graph.
website = "https://pixe.la/v1/users/rastog18/graphs/graph1.html"
id = "graph1"

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_header = {"X-USER-TOKEN": password}
graph_parameter = {"id": "graph1",
                   "name": "Weight Loss",
                   "unit": "Kg",
                   "type": "float",
                   "color": "ajisai"}

# response2 = requests.post(url=graph_endpoint, json=graph_parameter, headers=graph_header)
# print(response2.text)

# TODO-3 Post a value to pixela Graph.

clock = dt.datetime.now().strftime("%Y%m%d")
weight = str(input("Enter your weight:"))

postgraph_endpoint = f"{graph_endpoint}/{id}"
postgraph_parameter = {"date": "20230625",
                       "quantity": weight}
# response3 = requests.post(url=postgraph_endpoint,json=postgraph_parameter,headers=graph_header)
# response3.raise_for_status()

# TODO-4 Update a value from the Graph.
putgraph_parameter = {"quantity": "80.32"}
# response4 = requests.put(url=f"{postgraph_endpoint}/20230625", headers=graph_header, json=putgraph_parameter)
# response4.raise_for_status()

# TODO-5 Delete a value from the Graph.
# response5 = requests.delete(url=f"{postgraph_endpoint}/20230627",headers=graph_header)
# response5.raise_for_status()