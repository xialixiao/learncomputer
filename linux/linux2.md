## 二、前后台
# （1）&（终端关闭，程序也关闭）
command &：使用后台进程模式执行 command
Ctrl+Z：将当前进程放到后台（但程序是Stopped状态）
jobs：查看任务（状态、ID等）
fg n：将jobID为n的任务切到前台运行
bg n：将jobID为n的任务切到后台运行
# （2）nohup（终端关闭，程序继续运行）
nohup command &：后台执行 command，标准输出到 nohup.out
nohup command > log_file &：后台执行 command，标准输出到 log_file
nohup command > log_file 2>&1 &：后台执行 command，标准输出和错误输出到 log_file
nohup command > log_file 2>err_log &：后台执行 command，标准输出到 log_file，错误输出到 err_log
ps/kill：查看进程/结束进程
# （3）screen（创建独立会话）
screen -S my_session：创建一个名为 my_session 的会话
screen -ls：列出当前所有的 session
screen -r my_session：重新连接 my_session 这个会话
screen -d my_session：脱离 my_session 这个会话
Ctrl+a+d：在 screen 中，脱离当前会话
exit：在 screen 中，退出并删除当前 screen
-X -S my_session quit：删除 my_session 这个会话
screen -wipe：删除所有已经失效的会话