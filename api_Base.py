from playwright.sync_api import Playwright
payload = {"orders": [{"country": "India","productOrderedId": "68a961459320a140fe1ca57a"}]}


class ApiUtils:

    def gettoken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail":"maheshbadakal8@gmail.com","userPassword":"Aa123456@#", "Content-Type": "application/json"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright):
        token = self.gettoken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=payload, headers= {"Authorization":token, "Content-Type": "application/json"})
        print(response.json())
        response_Body = response.json()
        orderId = response_Body["orders"][0]
        return orderId

