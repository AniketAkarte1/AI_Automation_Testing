from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(), additional_authorized_imports=[
    "selenium",
    "selenium.webdriver.common.keys",
    "selenium.webdriver.common.by",
    "webdriver_manager.chrome"

])

agent.run("write a Selenium test to run test in headful mode for https://mail.google.com/ website to perform login operation and then navigate to Employee list and create new user with some realistic data")
