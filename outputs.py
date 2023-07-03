import requests as req
import json


class outputs_plans:
    """
    This class will report You the production plans region and their Zyrrus
    Status. the output of first function collected all the regions with their zyrrus. second one takes region
    and give an url for redirect the user. in some part of functions, for example in osid, I use a hardcode vlue,
    because it is not important to define the url which client will see as a redirect page.
    """
    @staticmethod
    def plan(productID):
        plan_output = []
        plan_url = f"https://cloudzy.com/api/regions?productId={productID}&slug=home"
        plan_response = req.get(plan_url)
        plan_response_json = plan_response.json()
        for region in plan_response_json:
            id_region = region['id']
            is_Zyrrus = region['isZyrrus']
            plan_region = [id_region,is_Zyrrus]
            plan_output.append(plan_region)
        return plan_output
    @staticmethod
    def submit_plan(productionID,regionID):
        submit_url = "https://cloudzy.com/api/submit"
        payload = json.dumps({
            "productId": productionID,
            "selectedProductId": productionID,
            "regionConfigId": None,
            "regionId": regionID,
            "ram": 8,
            "estimatedTotal": 3.95,
            "osFamily": "ubuntu",
            "osId": "3100a27357a0133a145f2843afc697ce6f883940e0e6d342e335bc6b9c6c4d10",
            "osConfigId": None,
            "selectedSlug": "home",
            "selectedFeature": None
        })
        submit_response = req.post(submit_url,data = payload)
        submit_response_json = submit_response.json()
        return submit_response_json['redirect_url'][0:9]






