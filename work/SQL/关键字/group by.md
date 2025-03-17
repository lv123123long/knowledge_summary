# group by

group by 是sql中用于将具有相同值的行分组的一个子句

通常和 COUNT()

SUM()

AVG()

MAX()

MIN()  等一起使用

## 分组

group by 子句 用于根据一个或多个列的值 对数据进行分组。所有具有相同值的行会被归为一组

## 聚合

通常与聚合函数结合 使用来执行一些统计操作。例如计算每组的数量，求和，平均值等


## 示例

### 示例1
求每个部门的员工数量
假设有表 `employees`，包含字段 `id`, `name`, `department`。我们想要知道每个部门有多少名员工。

```

```


### 示例2
求每门课程最高分

假设有一个成绩表 scores，包含字段 id, course, score。我们想要找出每个课程的最高分数


### 示例3
结合条件筛选特定组

如果我们只关心某些特定的组，可以结合 HAVING 子句使用。例如，找出至少有两名学生的课程。


## 注意事项

选择列表中的非聚合列必须出现在 GROUP BY 子句中：在 SELECT 语句中，如果包含了不在聚合函数中的列，这些列也必须出现在 GROUP BY 子句中。
Sql
深色版本
-- 错误示例
```
SELECT name, department, COUNT(*) FROM employees GROUP BY department;
```


-- 正确示例
```
SELECT name, department, COUNT(*) FROM employees GROUP BY department, name;
```

聚合函数不能直接作用于被分组的列：对于已经被 GROUP BY 分组的列，不能再直接应用聚合函数，但可以在同一查询中对其他列使用聚合函数。
HAVING 与 WHERE 的区别：WHERE 过滤的是分组之前的记录，而 HAVING 是用来过滤分组后的结果。也就是说，HAVING 可以基于聚合函数的结果进行筛选。




```
SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department;
```


```
SELECT course, MAX(score) AS highest_score FROM scores GROUP BY course;
```


```
SELECT course, COUNT(*) AS student_count FROM scores GROUP BY course HAVING COUNT(*) >= 2;
```






