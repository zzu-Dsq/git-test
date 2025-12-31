# 收敛曲线对比工具 / Convergence Curve Comparison Tool

这个工具用于模拟和比较不同优化算法的收敛速度。

This tool is used to simulate and compare the convergence speed of different optimization algorithms.

## 功能特性 / Features

- 模拟4种不同的优化算法：
  - Adam优化器 (Adam Optimizer)
  - 快速梯度下降 (Fast Gradient Descent with Momentum)
  - 标准梯度下降 (Standard Gradient Descent)
  - 基础梯度下降 (Basic Gradient Descent)

- 生成可视化收敛曲线对比图
- 提供详细的收敛速度统计信息

## 安装依赖 / Installation

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install numpy matplotlib
```

## 使用方法 / Usage

直接运行Python脚本：

```bash
python convergence_comparison.py
```

或者如果已设置执行权限：

```bash
chmod +x convergence_comparison.py
./convergence_comparison.py
```

## 输出 / Output

程序会生成：
1. `convergence_comparison.png` - 收敛曲线对比图
2. 控制台输出 - 详细的收敛速度统计信息

## 示例输出 / Example Output

运行脚本后，你将看到：
- 一个包含4条不同颜色曲线的图表，展示不同算法的收敛过程
- 每个算法的最终损失值、收敛所需迭代次数等统计信息

## 自定义 / Customization

你可以修改脚本中的参数来自定义模拟：
- `iterations`: 修改迭代次数（默认100次）
- 各个函数中的衰减率和噪声参数

## 技术说明 / Technical Notes

- 使用对数刻度显示Y轴，更好地展示收敛过程
- 添加了随机噪声模拟真实训练过程中的波动
- 支持中英文双语输出
