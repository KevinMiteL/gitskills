import numpy as np

# 创建一个一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print("一维数组:")
print(arr1)

# 创建一个二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组:")
print(arr2)

# 计算数组元素的和
sum_arr1 = np.sum(arr1)
print("数组元素的和:", sum_arr1)

# 计算数组元素的平均值
mean_arr2 = np.mean(arr2)
print("数组元素的平均值:", mean_arr2)

# 矩阵乘法
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
result_mat = np.dot(mat1, mat2)
print("矩阵乘法的结果:")
print(result_mat)
