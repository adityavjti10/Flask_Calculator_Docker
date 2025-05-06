const { Builder, By, until } = require('selenium-webdriver');
const assert = require('assert');

describe('login', function () {
  this.timeout(60000);

  let driver;

  beforeEach(async function () {
    driver = await new Builder().forBrowser('chrome').build();
  });

  afterEach(async function () {
    if (driver) {
      await driver.quit();
    }
  });

  it('login', async function () {
    await driver.get('http://localhost:5000/login');
    await driver.manage().window().setRect({ width: 1058, height: 850 });

    await driver.wait(until.elementLocated(By.name('username')), 10000);
    await driver.findElement(By.name('username')).sendKeys('aditya');
    await driver.findElement(By.name('password')).sendKeys('aditya');
    await driver.findElement(By.css('.btn-success')).click();

    // Wait for calculator form to load
    await driver.wait(until.elementLocated(By.name('num1')), 10000);

    // ➕ First Operation
    await driver.findElement(By.name('num1')).sendKeys('1');
    await driver.findElement(By.name('num2')).sendKeys('8');
    await driver.findElement(By.css('.btn-primary')).click();

    // 🔁 Re-locate elements after form is re-rendered
    await driver.wait(until.elementLocated(By.name('operation')), 10000);
    const operationDropdown = await driver.findElement(By.name('operation'));
    await operationDropdown.findElement(By.xpath("//option[. = 'Subtract']")).click();

    await driver.findElement(By.name('num1')).clear();
    await driver.findElement(By.name('num1')).sendKeys('2');
    await driver.findElement(By.name('num2')).clear();
    await driver.findElement(By.name('num2')).sendKeys('6');
    await driver.findElement(By.css('.btn-primary')).click();
  });
});
