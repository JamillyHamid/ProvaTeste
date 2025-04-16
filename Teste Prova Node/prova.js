const { Builder, By } = require('selenium-webdriver');
require('chromedriver');
const fs = require('fs');
const assert = require('assert');

(async function testeHanked() {
const url = 'https://www.hankeds.com.br/prova/login2.html';
let driver = await new Builder().forBrowser('chrome').build();

try {

await driver.get(url); //Recebe a URL do site
await driver.sleep(2000); //Tempo máximo de resposta 

//Encontra os elementos necessários
const username = await driver.findElement(By.id('username')); 
const password = await driver.findElement(By.id('password'));
const botao = await driver.findElement(By.xpath("//button[contains(text(),'Entrar')]"));

//Define a escrita devagar
for (const letra of 'admin') {
await username.sendKeys(letra);
await driver.sleep(250);
}

await driver.sleep(1000); //Tempo máximo de resposta 

//Define a escrita devagar
for (const letra of 'admin123456') {
await password.sendKeys(letra);
await driver.sleep(250);
}

await driver.sleep(1000); //Tempo máximo de resposta 
await botao.click();

await driver.sleep(4000); //Tempo máximo de resposta 

const urlAtual = await driver.getCurrentUrl();

//Condição para mostrar no terminal que o teste passou
if (urlAtual.includes('destino.html')) {
console.log(' Teste passou: redirecionado corretamente.');
} else {
console.log(' Teste falhou: não houve redirecionamento.');
}

await driver.sleep(5000);

} catch (err) {
console.error(' Erro durante o teste:', err); //Se der um erro não esperado
} finally {
await driver.quit(); 
}
})();