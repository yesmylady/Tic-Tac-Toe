# Tic-Tac-Toe
A simple game made with python and pygame
有python3和pygame环境即可直接运行main.py文件
ai算法：给所有可行点评分，根据该点所处所有路线中的情况而定。走评分最高的点。

ucb井字棋残次品.py : 尝试使用ucb公式代替之前的位置评估算法，对每个可行点进行固定次数的随机模拟，根据每次模拟的结果更新节点的ucb值，最后走ucb值最高的位置。
但效果并不理想，简单的ucb算法可能并不适用井字棋，当然也有可能是我个人代码问题。
