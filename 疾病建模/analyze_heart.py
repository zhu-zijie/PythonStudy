import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

# 过滤特定的numpy警告
warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy')

# 读取数据
df_heart = pd.read_csv("/Users/zhuzijie/Desktop/heart.csv")


# 改进的数据清理函数
def clean_data(df):
    df_clean = df.copy()

    # 处理无穷大值和NaN值
    df_clean = df_clean.replace([np.inf, -np.inf], np.nan)

    # 数据类型转换
    df_clean['FastingBS'] = df_clean['FastingBS'].map({0: 'Normal (≤120)', 1: 'High (>120)'})
    df_clean['HeartDisease'] = df_clean['HeartDisease'].map({0: 'No', 1: 'Yes'})
    df_clean['ExerciseAngina'] = df_clean['ExerciseAngina'].map({'N': 'No', 'Y': 'Yes'})

    # 获取数值列
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        # 特殊处理已知的异常值字段
        if col in ['RestingBP', 'Cholesterol']:
            # 将0值替换为NaN
            df_clean[col] = df_clean[col].replace(0, np.nan)

        # 使用中位数填充NaN值
        median_val = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(median_val)

        # 处理极端异常值（使用IQR方法）
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # 将极端值限制在合理范围内
        df_clean[col] = df_clean[col].clip(lower=lower_bound, upper=upper_bound)

    return df_clean


# 清理数据
df_heart = clean_data(df_heart)

# 保存处理后的数据
df_heart.to_csv("cleaned_heart.csv", index=False)

# 检查数据
print("数据基本信息:")
print(df_heart.info())
print("\n数据描述统计:")
print(df_heart.describe())
print("\n缺失值检查:")
print(df_heart.isnull().sum())

# 设置matplotlib参数避免字体警告
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 可视化：心脏病与年龄的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_heart, x="Age", hue="HeartDisease", kde=True, stat="density")
plt.title("Age Distribution by Heart Disease Status")
plt.savefig("heart_age_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：心脏病与性别的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_heart, x="Sex", hue="HeartDisease")
plt.title("Sex Distribution by Heart Disease Status")
plt.savefig("heart_sex_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：性别与心脏病的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_heart, x="ChestPainType", hue="HeartDisease")
plt.title("Chest Pain Type Distribution by Heart Disease Status")
plt.xticks(rotation=45)
plt.savefig("heart_chest_pain_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：静息心电图与心脏病的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_heart, x="RestingECG", hue="HeartDisease")
plt.title("Resting ECG Distribution by Heart Disease Status")
plt.savefig("heart_resting_ecg_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：运动心绞痛与心脏病的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_heart, x="ExerciseAngina", hue="HeartDisease")
plt.title("Exercise Angina Distribution by Heart Disease Status")
plt.savefig("heart_exercise_angina_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：ST斜率与心脏病的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_heart, x="ST_Slope", hue="HeartDisease")
plt.title("ST Slope Distribution by Heart Disease Status")
plt.savefig("heart_st_slope_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：空腹血糖与心脏病的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_heart, x="FastingBS", hue="HeartDisease")
plt.title("Fasting Blood Sugar Distribution by Heart Disease Status")
plt.savefig("heart_fasting_bs_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：静息血压与心脏病的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_heart, x="RestingBP", hue="HeartDisease", kde=True)
plt.title("Resting Blood Pressure Distribution by Heart Disease Status")
plt.savefig("heart_resting_bp_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：胆固醇与心脏病的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_heart, x="Cholesterol", hue="HeartDisease", kde=True)
plt.title("Cholesterol Distribution by Heart Disease Status")
plt.savefig("heart_cholesterol_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：最大心率与心脏病的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_heart, x="MaxHR", hue="HeartDisease", kde=True)
plt.title("Maximum Heart Rate Distribution by Heart Disease Status")
plt.savefig("heart_max_hr_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：Oldpeak与心脏病的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_heart, x="Oldpeak", hue="HeartDisease", kde=True)
plt.title("Oldpeak Distribution by Heart Disease Status")
plt.savefig("heart_oldpeak_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：心脏病与分类特征的关系
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
sns.countplot(data=df_heart, x="Sex", hue="HeartDisease", ax=axes[0, 0])
sns.countplot(data=df_heart, x="ChestPainType", hue="HeartDisease", ax=axes[0, 1])
sns.countplot(data=df_heart, x="RestingECG", hue="HeartDisease", ax=axes[0, 2])
sns.countplot(data=df_heart, x="ExerciseAngina", hue="HeartDisease", ax=axes[1, 0])
sns.countplot(data=df_heart, x="ST_Slope", hue="HeartDisease", ax=axes[1, 1])
sns.countplot(data=df_heart, x="FastingBS", hue="HeartDisease", ax=axes[1, 2])

# 设置标题
axes[0, 0].set_title("Sex")
axes[0, 1].set_title("Chest Pain Type")
axes[0, 2].set_title("Resting ECG")
axes[1, 0].set_title("Exercise Angina")
axes[1, 1].set_title("ST_Slope")
axes[1, 2].set_title("Fasting Blood Sugar")

plt.tight_layout()
plt.savefig("heart_categorical_features.png")
plt.close()

# 可视化：心脏病与数值特征的关系
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
sns.histplot(data=df_heart, x="RestingBP", hue="HeartDisease", kde=True, ax=axes[0, 0])
sns.histplot(data=df_heart, x="Cholesterol", hue="HeartDisease", kde=True, ax=axes[0, 1])
sns.histplot(data=df_heart, x="Age", hue="HeartDisease", kde=True, ax=axes[0, 2])
sns.histplot(data=df_heart, x="MaxHR", hue="HeartDisease", kde=True, ax=axes[1, 0])
sns.histplot(data=df_heart, x="Oldpeak", hue="HeartDisease", kde=True, ax=axes[1, 1])

axes[0, 0].set_title("Resting BP")
axes[0, 1].set_title("Cholesterol")
axes[0, 2].set_title("Age")
axes[1, 0].set_title("Max HR")
axes[1, 1].set_title("Oldpeak")

# 隐藏未使用的子图
axes[1, 2].set_visible(False)

plt.tight_layout()
plt.savefig("heart_numerical_features.png")
plt.close()

print("所有图表已生成完成！")
