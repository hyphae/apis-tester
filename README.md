# apis-tester

## Introduction  
APIS Tester is a tool for testing and evaluation of APIS. It can be used to evaluate energy sharing and to schedule automatic execution of error processing evaluation and log the evaluation results. APIS Tester uses apis-web, which is connected by a communication line such as Ethernet, and the Web API provided by DC/DC converter device drivers to perform the operations needed for evaluation 

![キャプチャ](https://user-images.githubusercontent.com/71874910/102714663-a1a02a00-4313-11eb-9179-7e3e3314e7fe.PNG)

## Installation

Here is how to install apis-dcdc_batt_comm individually.   

```bash
$ git clone https://github.com/SonyCSL/apis-tester.git
$ cd apis-tester
$ bash venvsh
```

## Running

Here is how to run apis-dcdc_batt_comm individually.  

*By default, 2 USB-RS485 converters are required for /dev/ttyUSB0 and /dev/ttyUSB1.  
See apis-dcdc_batt_comm's [Document](https://github.com/SonyCSL/apis-dcdc_batt_comm/blob/master/doc/jp/apis-dcdc_batt_comm_specification.md) for more information.

```bash
$ cd apis-tester
$ . venv/bin/activate
$ sudo python3 startTester.py
```

## Stopping
Here is how to stop apis-dcdc_batt_comm individually.  

```bash
$ cd apis-dcdc_batt_comm/drivers
$ bash stop.sh
$ deactivate
```

## Documentation

## License
&emsp;[Apache License Version 2.0](https://github.com/SonyCSL/apis-tester/blob/main/LICENSE)


## Notice
&emsp;[Notice](https://github.com/SonyCSL/apis-tester/blob/main/NOTICE.md)
