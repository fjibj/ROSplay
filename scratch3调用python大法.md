scratch-backplane本地环境搭建

![架构图](https://mryslab.github.io/s3-extend/images/s3onegpio.png)

（1）scratch部分

git clone https://github.com/fjibj/s3onegpio  （扩展了s3onegpioNl)

cd s3onegpio

npm install yarn

cd scratch-gui

yarn unlink scratch-vm

cd scratch-vm

yarn unlink

yarn --force install

yarn link

cd scratch-gui

yarn link scratch-vm

yarn --force install

yarn start（后续再启动只在scratch-gui目录下需要执行这一条）

在浏览器：http://localhost:8601/


（2）s3-extend

git clone https://github.com/fjibj/s3-extend （扩展了nl_gateway)

cd s3-extend

pip install .

单条命令运行：s3n

分别（在不同cmd窗口）运行：（本地调试用）

1. backplane （必须先启动）

2. wgsw -i 9001

3. nlgw (或cd s3_extend\gateways再运行python nl_gateway.py）


（3）关键代码：

正向消息传递：scratch_vm（index.js） --> wsgs --> backplane --> nl_gateway

scratch端对应代码：scratch-vm/src/extensions/scratch3_onegpioNl/index.js (操作块：return { ... blocks:[.....]})

extend端对应代码：s3_extend/gateways/nl_gateway.py （输出日志 C:\Users\当前Windows用户\nlgw.log，additional_banyan_messages()中添加自定义方法）

反向消息传递：nl_gateway --> backplane --> wsgs --> scratch_vm（index.js）

在 nl_gateway.py里面用

payload = {'report': 'sonar_data', 'value': distance} 

 self.publish_payload(payload, 'from_nl_gateway') 
 
对应的在scratch-vm/src/extensions/scratch3_onegpioNl/index.js中

window.socketr.onmessage = function (message) { 

msg = JSON.parse(message.data); 

let report_type = msg["report"]; 

，，，，，，，

} else if (report_type === 'sonar_data') { 

	value = msg['value']; 
  
	digital_inputs[sonar_report_pin] = value; 
  
} 

来接收消息，这种方式可以用于在scratch中定义一个变量，变量的值由python程序返回的情况，全局变量可以给后续其他块用。

（4）附：scratch3扩展插件开发

https://github.com/MrYsLab/s3onegpio/blob/master/scratch-vm/src/extensions/scratch3_onegpioNl/index.js

blockIconURI是base64格式的小图片，放在每个block的左边部分

https://github.com/MrYsLab/s3onegpio/blob/master/scratch-vm/src/extension-support/extension-manager.js

onegpioNl: () => require('../extensions/scratch3_onegpioNl'),

https://github.com/MrYsLab/s3onegpio/blob/master/scratch-gui/src/lib/libraries/extensions/onegpioNl/onegpioNl.png

https://github.com/MrYsLab/s3onegpio/blob/master/scratch-gui/src/lib/libraries/extensions/onegpioNl/onegpioNl-small.png

https://github.com/MrYsLab/s3onegpio/blob/master/scratch-gui/src/lib/libraries/extensions/index.jsx

import onegpioNlImage from './onegpioNl/onegpioNl.png';

import onegpioNlInsetIconURL from './onegpioNl/onegpioNl-small.png';


    {
    
        name: 'OneGpio Newland',
        
        extensionId: 'onegpioNl',
        
        collaborator: "Mr. Y's Lab",
        
        iconURL: onegpioNlImage,
        
        insetIconURL: onegpioNlInsetIconURL,
        
        description: 'OneGPIONl',
        
        featured: true,
        
        disabled: false,
        
        internetConnectionRequired: true,
        
        bluetoothRequired: false,
        
        helpLink: 'https://mryslab.github.io/s3-extend/'

    }

（5）scratch部分可以使用静态文件发布，即将s3onegpio用npm build或yarn build编译。

注：github上的gh-pages分支就是npm build或yarn build后生成的静态文件（不含Nl扩展）。


