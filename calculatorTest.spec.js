import { Builder, By } from "selenium-webdriver";
import chrome from "selenium-webdriver/chrome";
import assert from "assert";

describe("Calculator Test Suite", function () {
  this.timeout(40000); // Increased timeout
  let driver;

  before(async function () {
    this.timeout(10000); // Just for setup
    driver = await new Builder().forBrowser("chrome").setChromeOptions(new chrome.Options()).build();
    await driver.get("http://localhost:5000");
  });

  after(async function () {
    if (driver) {
      await driver.quit();
    }
  });

  it("Test Addition Operation", async function () {
    const num1Input = await driver.findElement(By.name("num1"));
    const num2Input = await driver.findElement(By.name("num2"));
    const addButton = await driver.findElement(By.id("add"));

    await num1Input.sendKeys("5");
    await num2Input.sendKeys("3");
    await addButton.click();

    await driver.sleep(1000); // Wait for result

    const result = await driver.findElement(By.id("result")).getText();
    assert.strictEqual(result, "Result: 8");
  });
});
