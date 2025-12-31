#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
收敛曲线对比工具
Convergence Curve Comparison Tool

该脚本模拟不同优化算法的收敛速度，并生成对比图表。
This script simulates the convergence speed of different optimization algorithms and generates comparison charts.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
# Set Chinese font support
rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans', 'SimHei']
rcParams['axes.unicode_minus'] = False


def gradient_descent_fast(iterations):
    """
    快速收敛算法 - 模拟带动量的梯度下降
    Fast convergence algorithm - Simulating gradient descent with momentum
    """
    loss = []
    initial_loss = 100.0
    loss_value = initial_loss
    
    for i in range(iterations):
        # 快速指数衰减
        loss_value = initial_loss * np.exp(-0.1 * i) + np.random.normal(0, 0.5)
        loss.append(max(loss_value, 0.01))  # 确保损失不为负
    
    return np.array(loss)


def gradient_descent_medium(iterations):
    """
    中等收敛算法 - 模拟标准梯度下降
    Medium convergence algorithm - Simulating standard gradient descent
    """
    loss = []
    initial_loss = 100.0
    loss_value = initial_loss
    
    for i in range(iterations):
        # 中等速度衰减
        loss_value = initial_loss * np.exp(-0.05 * i) + np.random.normal(0, 1.0)
        loss.append(max(loss_value, 0.01))
    
    return np.array(loss)


def gradient_descent_slow(iterations):
    """
    慢速收敛算法 - 模拟基础梯度下降
    Slow convergence algorithm - Simulating basic gradient descent
    """
    loss = []
    initial_loss = 100.0
    loss_value = initial_loss
    
    for i in range(iterations):
        # 慢速衰减
        loss_value = initial_loss / (1 + 0.05 * i) + np.random.normal(0, 1.5)
        loss.append(max(loss_value, 0.01))
    
    return np.array(loss)


def adam_optimizer(iterations):
    """
    Adam优化器 - 自适应学习率
    Adam optimizer - Adaptive learning rate
    """
    loss = []
    initial_loss = 100.0
    loss_value = initial_loss
    
    for i in range(iterations):
        # Adam风格的快速收敛，带有早期振荡
        if i < 10:
            loss_value = initial_loss * (1 - 0.1 * i / 10) + np.random.normal(0, 5)
        else:
            loss_value = initial_loss * np.exp(-0.12 * (i - 10)) + np.random.normal(0, 0.3)
        loss.append(max(loss_value, 0.01))
    
    return np.array(loss)


def plot_convergence_curves(iterations=100):
    """
    绘制收敛曲线对比图
    Plot convergence curve comparison
    
    Args:
        iterations: 迭代次数 / Number of iterations
    """
    # 生成数据
    x = np.arange(iterations)
    
    # 模拟不同算法的收敛过程
    adam_loss = adam_optimizer(iterations)
    fast_loss = gradient_descent_fast(iterations)
    medium_loss = gradient_descent_medium(iterations)
    slow_loss = gradient_descent_slow(iterations)
    
    # 创建图表
    plt.figure(figsize=(12, 8))
    
    # 绘制收敛曲线
    plt.plot(x, adam_loss, label='Adam优化器 (Adam Optimizer)', 
             linewidth=2, marker='o', markevery=10, markersize=5)
    plt.plot(x, fast_loss, label='快速梯度下降 (Fast GD with Momentum)', 
             linewidth=2, marker='s', markevery=10, markersize=5)
    plt.plot(x, medium_loss, label='标准梯度下降 (Standard GD)', 
             linewidth=2, marker='^', markevery=10, markersize=5)
    plt.plot(x, slow_loss, label='基础梯度下降 (Basic GD)', 
             linewidth=2, marker='d', markevery=10, markersize=5)
    
    # 设置图表属性
    plt.xlabel('迭代次数 (Iterations)', fontsize=12)
    plt.ylabel('损失值 (Loss Value)', fontsize=12)
    plt.title('优化算法收敛速度对比\nOptimization Algorithm Convergence Speed Comparison', 
              fontsize=14, fontweight='bold')
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.yscale('log')  # 使用对数刻度更好地展示收敛过程
    
    # 保存图表
    plt.tight_layout()
    plt.savefig('convergence_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ 收敛曲线图已保存为 'convergence_comparison.png'")
    print("✓ Convergence curve saved as 'convergence_comparison.png'")
    
    plt.show()
    
    # 打印统计信息
    print("\n" + "="*60)
    print("收敛速度统计 (Convergence Speed Statistics)")
    print("="*60)
    
    algorithms = {
        'Adam优化器': adam_loss,
        '快速梯度下降': fast_loss,
        '标准梯度下降': medium_loss,
        '基础梯度下降': slow_loss
    }
    
    for name, loss_values in algorithms.items():
        # 计算收敛到初始损失10%所需的迭代次数
        threshold = loss_values[0] * 0.1
        converged_at = np.where(loss_values < threshold)[0]
        if len(converged_at) > 0:
            iterations_to_converge = converged_at[0]
        else:
            iterations_to_converge = iterations
        
        final_loss = loss_values[-1]
        print(f"\n{name}:")
        print(f"  - 最终损失值: {final_loss:.4f}")
        print(f"  - 收敛到10%阈值所需迭代数: {iterations_to_converge}")
        print(f"  - 平均收敛速度: {(loss_values[0] - final_loss) / iterations:.4f}/迭代")


def main():
    """主函数"""
    print("="*60)
    print("收敛曲线对比模拟工具")
    print("Convergence Curve Comparison Simulation")
    print("="*60)
    print("\n正在生成收敛曲线...")
    print("Generating convergence curves...\n")
    
    # 设置迭代次数
    iterations = 100
    
    # 绘制收敛曲线
    plot_convergence_curves(iterations)
    
    print("\n✓ 模拟完成！")
    print("✓ Simulation completed!")


if __name__ == "__main__":
    main()
