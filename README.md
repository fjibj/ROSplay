# ROSplay
ROS机器人学习、创作

xf_voice_speak 中文语音控制机器人运动

思路：先把语音转换成文字，然后文字与动作对应，动作再驱动机器人运动

（1）创建record_speak.cpp，通过修改iat_publish_speak.cpp(科大讯飞)，并将文字输出到xfspeech主题

参考：http://blog.csdn.net/zhouge94/article/details/52333908

新开终端1

$ roscore 

新开终端2: (订阅xfwakeup主题，发布xfspeech主题和xfwords主题)

$ rosrun xf_voice_robot record_speak

新开终端3：（xfspeech主题是录音专成的文字）

$ rostopic echo /xfspeech

新开终端4：（xfwords主题是错误提示文字）

$ rostopic echo /xfwords

（2）创建my_voice_nav.py(通过修改voice_nav.py)，订阅xfspeech主题，（触发回调函数）将识别出的中文与动作对应

启动模拟器

$ roslaunch rbx1_bringup fake_turtlebot.launch

$ rosrun rviz rviz -d \`rospack find rbx1_nav\`/sim.rviz

运行voice_nav节点

$ roslaunch xf_voice_robot turtlebot_voice_nav.launch

