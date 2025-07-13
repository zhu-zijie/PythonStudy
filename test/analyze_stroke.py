import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

# 过滤警告
warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy')

# 读取数据
df_stroke = pd.read_csv("/Users/zhuzijie/Desktop/stroke.csv")

print("原始数据信息:")
print(df_stroke.info())
print(f"\n原始数据形状: {df_stroke.shape}")

# 检查ID字段重复情况
if 'id' in df_stroke.columns:
    total_rows = len(df_stroke)
    unique_ids = df_stroke['id'].nunique()
    duplicate_ids = df_stroke['id'].duplicated().sum()

    print(f"\nID字段检查:")
    print(f"总行数: {total_rows}")
    print(f"唯一ID数: {unique_ids}")
    print(f"重复ID数: {duplicate_ids}")

    if duplicate_ids > 0:
        print(f"\n发现{duplicate_ids}个重复ID，正在处理...")
        # 显示重复的ID
        duplicate_id_values = df_stroke[df_stroke['id'].duplicated(keep=False)]['id'].unique()
        print(f"重复的ID值: {duplicate_id_values[:10]}")  # 只显示前10个

        # 保留每个ID的第一条记录，删除重复行
        df_stroke = df_stroke.drop_duplicates(subset=['id'], keep='first')
        print(f"删除重复行后数据形状: {df_stroke.shape}")
    else:
        print("ID字段无重复记录")


# 数据清理函数
def clean_stroke_data(df):
    df_clean = df.copy()

    # 删除id字段
    if 'id' in df_clean.columns:
        df_clean = df_clean.drop('id', axis=1)

    # 检查gender字段并删除'Other'
    if 'gender' in df_clean.columns:
        print(f"\nGender字段值分布:")
        print(df_clean['gender'].value_counts())

        if 'Other' in df_clean['gender'].values:
            other_count = (df_clean['gender'] == 'Other').sum()
            print(f"发现{other_count}个'Other'记录，正在删除...")
            df_clean = df_clean[df_clean['gender'] != 'Other']
            print(f"删除'Other'后数据形状: {df_clean.shape}")

    # 数据类型转换
    df_clean['hypertension'] = df_clean['hypertension'].map({0: 'No', 1: 'Yes'})
    df_clean['heart_disease'] = df_clean['heart_disease'].map({0: 'No', 1: 'Yes'})
    df_clean['stroke'] = df_clean['stroke'].map({0: 'No', 1: 'Yes'})

    # 处理BMI字段的异常值
    if 'bmi' in df_clean.columns:
        print(f"\nBMI字段处理:")
        print(f"BMI数据类型: {df_clean['bmi'].dtype}")
        print(f"BMI唯一值样例: {df_clean['bmi'].unique()[:10]}")

        # 转换BMI为数值类型
        df_clean['bmi'] = pd.to_numeric(df_clean['bmi'], errors='coerce')

        # 处理BMI异常值（正常BMI范围：10-60）
        print(f"BMI描述统计: {df_clean['bmi'].describe()}")

        # 标记异常值
        bmi_outliers = (df_clean['bmi'] < 10) | (df_clean['bmi'] > 60)
        outlier_count = bmi_outliers.sum()
        if outlier_count > 0:
            print(f"发现{outlier_count}个BMI异常值")
            print(f"异常BMI值: {df_clean.loc[bmi_outliers, 'bmi'].values}")
            # 将异常值设为NaN
            df_clean.loc[bmi_outliers, 'bmi'] = np.nan

        # 用均值填充缺失值
        bmi_missing = df_clean['bmi'].isna().sum()
        if bmi_missing > 0:
            bmi_mean = df_clean['bmi'].mean()
            print(f"BMI均值: {bmi_mean:.2f}")
            df_clean['bmi'] = df_clean['bmi'].fillna(bmi_mean)
            print(f"已用均值填充{bmi_missing}个BMI缺失值")

    # 处理年龄异常值
    if 'age' in df_clean.columns:
        print(f"\n年龄字段处理:")
        print(f"年龄描述统计: {df_clean['age'].describe()}")

        # 年龄异常值（合理范围：0-120）
        age_outliers = (df_clean['age'] < 0) | (df_clean['age'] > 120)
        outlier_count = age_outliers.sum()
        if outlier_count > 0:
            print(f"发现{outlier_count}个年龄异常值")
            print(f"异常年龄值: {df_clean.loc[age_outliers, 'age'].values}")
            # 将异常值设为中位数
            age_median = df_clean['age'].median()
            df_clean.loc[age_outliers, 'age'] = age_median
            print(f"已将异常年龄值替换为中位数: {age_median}")

    # 处理平均血糖水平异常值
    if 'avg_glucose_level' in df_clean.columns:
        print(f"\n血糖水平字段处理:")
        print(f"血糖水平描述统计: {df_clean['avg_glucose_level'].describe()}")

        # 使用IQR方法检测异常值
        Q1 = df_clean['avg_glucose_level'].quantile(0.25)
        Q3 = df_clean['avg_glucose_level'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        glucose_outliers = (df_clean['avg_glucose_level'] < lower_bound) | (df_clean['avg_glucose_level'] > upper_bound)
        outlier_count = glucose_outliers.sum()

        if outlier_count > 0:
            print(f"IQR方法检测到{outlier_count}个血糖异常值")
            print(f"合理范围: [{lower_bound:.1f}, {upper_bound:.1f}]")
            # 将异常值限制在合理范围内
            df_clean['avg_glucose_level'] = df_clean['avg_glucose_level'].clip(lower=lower_bound, upper=upper_bound)
            print("已将异常值限制在合理范围内")

    # 处理其他数值字段的异常值和缺失值（可以舍去）
    # numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    #
    # for col in numeric_cols:
    #     if col not in ['age', 'bmi', 'avg_glucose_level']:  # 跳过已处理的字段
    #         print(f"\n处理字段 {col}:")
    #         print(f"{col} 描述统计: {df_clean[col].describe()}")
    #
    #         # 使用IQR方法检测异常值
    #         if df_clean[col].nunique() > 2:  # 只对连续变量进行异常值检测
    #             Q1 = df_clean[col].quantile(0.25)
    #             Q3 = df_clean[col].quantile(0.75)
    #             IQR = Q3 - Q1
    #
    #             if IQR > 0:  # 避免除零错误
    #                 lower_bound = Q1 - 1.5 * IQR
    #                 upper_bound = Q3 + 1.5 * IQR
    #
    #                 outliers = (df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)
    #                 outlier_count = outliers.sum()
    #
    #                 if outlier_count > 0:
    #                     print(f"发现{outlier_count}个{col}异常值")
    #                     # 将异常值限制在合理范围内
    #                     df_clean[col] = df_clean[col].clip(lower=lower_bound, upper=upper_bound)
    #                     print(f"已将{col}异常值限制在范围[{lower_bound:.2f}, {upper_bound:.2f}]内")
    #
    #         # 处理缺失值
    #         missing_count = df_clean[col].isna().sum()
    #         if missing_count > 0:
    #             if df_clean[col].nunique() > 2:
    #                 fill_value = df_clean[col].median()
    #                 method = "中位数"
    #             else:
    #                 fill_value = df_clean[col].mode()[0] if not df_clean[col].mode().empty else 0
    #                 method = "众数"
    #
    #             df_clean[col] = df_clean[col].fillna(fill_value)
    #             print(f"字段{col}: 用{method}{fill_value}填充了{missing_count}个缺失值")

    return df_clean


# 执行数据清理
df_stroke = clean_stroke_data(df_stroke)

# 保存处理后的数据
df_stroke.to_csv("cleaned_stroke.csv", index=False)

print(f"\n最终清理后数据信息:")
print(df_stroke.info())
print(f"最终数据形状: {df_stroke.shape}")
print(f"各字段缺失值统计:")
print(df_stroke.isnull().sum())

# 数据完整性检查
print(f"数据完整性: {(1 - df_stroke.isnull().sum().sum() / (df_stroke.shape[0] * df_stroke.shape[1])) * 100:.2f}%")
print(f"stroke字段分布: {df_stroke['stroke'].value_counts().to_dict()}")
if 'gender' in df_stroke.columns:
    print(f"gender字段分布: {df_stroke['gender'].value_counts().to_dict()}")

# 设置matplotlib参数避免字体警告
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 可视化：中风与高血压的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="hypertension", hue="stroke")
plt.title("Hypertension Distribution by Stroke Status")
plt.savefig("stroke_hypertension_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与心脏病的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="heart_disease", hue="stroke")
plt.title("Heart Disease Distribution by Stroke Status")
plt.savefig("stroke_heart_disease_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与婚姻状况的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="ever_married", hue="stroke")
plt.title("Marriage Status Distribution by Stroke Status")
plt.savefig("stroke_marriage_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与工作类型的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="work_type", hue="stroke")
plt.title("Work Type Distribution by Stroke Status")
plt.xticks(rotation=45)
plt.savefig("stroke_work_type_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与居住类型的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="Residence_type", hue="stroke")
plt.title("Residence Type Distribution by Stroke Status")
plt.savefig("stroke_residence_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与吸烟状况的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="smoking_status", hue="stroke")
plt.title("Smoking Status Distribution by Stroke Status")
plt.xticks(rotation=45)
plt.savefig("stroke_smoking_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与性别的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_stroke, x="gender", hue="stroke")
plt.title("Gender Distribution by Stroke Status")
plt.savefig("stroke_gender_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与BMI的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_stroke, x="bmi", hue="stroke", kde=True)
plt.title("BMI Distribution by Stroke Status")
plt.savefig("stroke_bmi_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与平均血糖水平的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_stroke, x="avg_glucose_level", hue="stroke", kde=True)
plt.title("Average Glucose Level Distribution by Stroke Status")
plt.savefig("stroke_glucose_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与年龄的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_stroke, x="age", hue="stroke", kde=True)
plt.title("Age Distribution by Stroke Status")
plt.savefig("stroke_age_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与分类特征的关系（综合图）
fig, axes = plt.subplots(3, 3, figsize=(18, 18))
sns.countplot(data=df_stroke, x="gender", hue="stroke", ax=axes[0, 0])
sns.countplot(data=df_stroke, x="hypertension", hue="stroke", ax=axes[0, 1])
sns.countplot(data=df_stroke, x="heart_disease", hue="stroke", ax=axes[0, 2])
sns.countplot(data=df_stroke, x="ever_married", hue="stroke", ax=axes[1, 0])
sns.countplot(data=df_stroke, x="work_type", hue="stroke", ax=axes[1, 1])
sns.countplot(data=df_stroke, x="Residence_type", hue="stroke", ax=axes[1, 2])
sns.countplot(data=df_stroke, x="smoking_status", hue="stroke", ax=axes[2, 0])

# 调整子图标题
axes[0, 0].set_title("Gender")
axes[0, 1].set_title("Hypertension")
axes[0, 2].set_title("Heart Disease")
axes[1, 0].set_title("Marriage Status")
axes[1, 1].set_title("Work Type")
axes[1, 2].set_title("Residence Type")
axes[2, 0].set_title("Smoking Status")

# 隐藏空子图
axes[2, 1].set_visible(False)
axes[2, 2].set_visible(False)

# 旋转x轴标签
# axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("stroke_categorical_features.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：中风与数值特征的关系（综合图）
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
sns.histplot(data=df_stroke, x="age", hue="stroke", kde=True, ax=axes[0])
sns.histplot(data=df_stroke, x="avg_glucose_level", hue="stroke", kde=True, ax=axes[1])
sns.histplot(data=df_stroke, x="bmi", hue="stroke", kde=True, ax=axes[2])

# 设置子图标题
axes[0].set_title("Age Distribution")
axes[1].set_title("Average Glucose Level Distribution")
axes[2].set_title("BMI Distribution")

plt.tight_layout()
plt.savefig("stroke_numerical_features.png", dpi=300, bbox_inches='tight')
plt.close()

print("所有图表已生成完成！")
