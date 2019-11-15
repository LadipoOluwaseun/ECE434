#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const VSERV = 'P9_14';
const button = 'P9_25';

b.pinMode(LED0, b.OUTPUT);
b.pinMode(VSERV, b.OUTPUT);
b.pinMode(button, b.INPUT);

const AUTH = 'es3WljyRao1a-bphIXsF93x-ZBiph0Pr';

var blynk = new Blynk.Blynk(AUTH);


var v0 = new blynk.VirtualPin(0);
var v1 = new blynk.VirtualPin(1);

var v2 = new blynk.setProperty(V1, "url", "https://www.youtube.com/watch?v=EngW7tLk6R8");

var v10 = new blynk.WidgetLED(10);

v0.on('write', function(param) {
    //var duty_cycle = param[0]/1023;
	var duty_cycle = param[0];
	console.log('Vertical:', duty_cycle);
	b.analogWrite(VSERV, duty_cycle);
});

v1.on('write', function(param) {
	//var duty_cycle = param[0]/1023;
	var duty_cycle = param[0];
	console.log('Horizontal:', duty_cycle);
	b.analogWrite(VSERV, duty_cycle);
});

v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}