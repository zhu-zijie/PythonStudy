import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

# 过滤警告
warnings.filterwarnings('ignore', category=RuntimeWarning, module='numpy')

# 读取数据
df_cirrhosis = pd.read_csv("/Users/zhuzijie/Desktop/cirrhosis.csv")

print("原始数据信息:")
print(df_cirrhosis.info())
print(f"\n原始数据形状: {df_cirrhosis.shape}")


# 检查ID字段重复情况
# if 'ID' in df_cirrhosis.columns:
#     total_rows = len(df_cirrhosis)
#     unique_ids = df_cirrhosis['ID'].nunique()
#     duplicate_ids = df_cirrhosis['ID'].duplicated().sum()
#
#     print(f"\nID字段检查:")
#     print(f"总行数: {total_rows}")
#     print(f"唯一ID数: {unique_ids}")
#     print(f"重复ID数: {duplicate_ids}")
#
#     if duplicate_ids > 0:
#         print(f"\n发现{duplicate_ids}个重复ID，正在处理...")
#         duplicate_id_values = df_cirrhosis[df_cirrhosis['ID'].duplicated(keep=False)]['ID'].unique()
#         print(f"重复的ID值: {duplicate_id_values[:10]}")
#
#         df_cirrhosis = df_cirrhosis.drop_duplicates(subset=['ID'], keep='first')
#         print(f"删除重复行后数据形状: {df_cirrhosis.shape}")
#     else:
#         print("ID字段无重复记录")


# 数据清理函数
def clean_cirrhosis_data(df):
    df_clean = df.copy()

    # 处理大量Nan值，以'Drug'字段为例
    df_clean = df_clean.dropna(subset=['Drug'])
    print("当前数据信息:")
    print(df_clean.info())
    print(f"\n原始数据形状: {df_clean.shape}")

    # 删除ID字段
    if 'ID' in df_clean.columns:
        df_clean = df_clean.drop('ID', axis=1)

    # 检查Status字段分布
    if 'Status' in df_clean.columns:
        print(f"\nStatus字段值分布:")
        print(df_clean['Status'].value_counts())

    # 将Stage转换为字符类型
    if 'Stage' in df_clean.columns:
        print(f"\nStage字段处理:")
        print(f"Stage原始值分布: {df_clean['Stage'].value_counts()}")

        # 处理缺失值后再转换
        stage_missing = df_clean['Stage'].isna().sum()
        if stage_missing > 0:
            stage_mode = df_clean['Stage'].mode()[0] if not df_clean['Stage'].mode().empty else 1
            df_clean['Stage'] = df_clean['Stage'].fillna(stage_mode)
            print(f"用众数{stage_mode}填充了{stage_missing}个Stage缺失值")

        # 转换为字符类型
        df_clean['Stage'] = df_clean['Stage'].astype(int).astype(str)
        df_clean['Stage'] = 'Stage ' + df_clean['Stage']
        print(f"Stage转换后分布: {df_clean['Stage'].value_counts()}")

    # 处理年龄异常值
    if 'Age' in df_clean.columns:
        print(f"\n年龄字段处理:")
        print(f"年龄描述统计: {df_clean['Age'].describe()}")

        age_outliers = (df_clean['Age'] < 0) | (df_clean['Age'] > 120)
        outlier_count = age_outliers.sum()
        if outlier_count > 0:
            print(f"发现{outlier_count}个年龄异常值")
            age_median = df_clean['Age'].median()
            df_clean.loc[age_outliers, 'Age'] = int(age_median)
            print(f"已将异常年龄值替换为中位数: {age_median}")

    # 处理数值字段的异常值和缺失值
    numeric_cols = ['Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos',
                    'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']

    for col in numeric_cols:
        if col in df_clean.columns:
            print(f"\n{col}字段处理:")
            print(f"{col}描述统计: {df_clean[col].describe()}")

            # 使用IQR方法检测异常值
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1

            if IQR > 0:
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                outliers = (df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)
                outlier_count = outliers.sum()

                if outlier_count > 0:
                    print(f"发现{outlier_count}个{col}异常值")
                    print(f"合理范围: [{lower_bound:.2f}, {upper_bound:.2f}]")
                    df_clean[col] = df_clean[col].clip(lower=lower_bound, upper=upper_bound)
                    print("已将异常值限制在合理范围内")

            # 处理缺失值
            missing_count = df_clean[col].isna().sum()
            if missing_count > 0:
                fill_value = df_clean[col].median()
                df_clean[col] = df_clean[col].fillna(fill_value)
                print(f"用中位数{fill_value:.2f}填充了{missing_count}个{col}缺失值")

    return df_clean


# 执行数据清理
df_cirrhosis = clean_cirrhosis_data(df_cirrhosis)

# 保存处理后的数据
df_cirrhosis.to_csv("cleaned_cirrhosis.csv", index=False)

print(f"\n最终清理后数据信息:")
print(df_cirrhosis.info())
print(f"最终数据形状: {df_cirrhosis.shape}")
print(f"各字段缺失值统计:")
print(df_cirrhosis.isnull().sum())

# 数据完整性检查
print(
    f"数据完整性: {(1 - df_cirrhosis.isnull().sum().sum() / (df_cirrhosis.shape[0] * df_cirrhosis.shape[1])) * 100:.2f}%")
print(f"Status字段分布: {df_cirrhosis['Status'].value_counts().to_dict()}")
if 'Sex' in df_cirrhosis.columns:
    print(f"Sex字段分布: {df_cirrhosis['Sex'].value_counts().to_dict()}")

# 设置matplotlib参数避免字体警告
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 可视化：肝硬化与性别的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Sex", hue="Status")
plt.title("Sex Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_sex_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与药物的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Drug", hue="Status")
plt.title("Drug Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_drug_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与腹水的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Ascites", hue="Status")
plt.title("Ascites Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_ascites_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与肝肿大的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Hepatomegaly", hue="Status")
plt.title("Hepatomegaly Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_hepatomegaly_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与蜘蛛痣的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Spiders", hue="Status")
plt.title("Spiders Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_spiders_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与水肿的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Edema", hue="Status")
plt.title("Edema Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_edema_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与Stage的关系
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cirrhosis, x="Stage", hue="Status")
plt.title("Stage Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_stage_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与天数的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="N_Days", hue="Status", kde=True)
plt.title("N_Days Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_days_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与年龄的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Age", hue="Status", kde=True)
plt.title("Age Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_age_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与胆红素的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Bilirubin", hue="Status", kde=True)
plt.title("Bilirubin Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_bilirubin_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与胆固醇的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Cholesterol", hue="Status", kde=True)
plt.title("Cholesterol Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_cholesterol_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与白蛋白的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Albumin", hue="Status", kde=True)
plt.title("Albumin Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_albumin_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与铜的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Copper", hue="Status", kde=True)
plt.title("Copper Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_copper_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与碱性磷酸酶的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Alk_Phos", hue="Status", kde=True)
plt.title("Alk_Phos Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_alk_phos_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与SGOT的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="SGOT", hue="Status", kde=True)
plt.title("SGOT Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_sgot_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与甘油三酯的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Tryglicerides", hue="Status", kde=True)
plt.title("Tryglicerides Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_tryglicerides_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与血小板的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Platelets", hue="Status", kde=True)
plt.title("Platelets Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_platelets_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与凝血酶原的关系
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cirrhosis, x="Prothrombin", hue="Status", kde=True)
plt.title("Prothrombin Distribution by Cirrhosis Status")
plt.savefig("cirrhosis_prothrombin_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与分类特征的关系（综合图）
fig, axes = plt.subplots(2, 4, figsize=(24, 12))
sns.countplot(data=df_cirrhosis, x="Sex", hue="Status", ax=axes[0, 0])
sns.countplot(data=df_cirrhosis, x="Drug", hue="Status", ax=axes[0, 1])
sns.countplot(data=df_cirrhosis, x="Ascites", hue="Status", ax=axes[0, 2])
sns.countplot(data=df_cirrhosis, x="Hepatomegaly", hue="Status", ax=axes[0, 3])
sns.countplot(data=df_cirrhosis, x="Spiders", hue="Status", ax=axes[1, 0])
sns.countplot(data=df_cirrhosis, x="Edema", hue="Status", ax=axes[1, 1])
sns.countplot(data=df_cirrhosis, x="Stage", hue="Status", ax=axes[1, 2])

# 设置子图标题
axes[0, 0].set_title("Sex")
axes[0, 1].set_title("Drug")
axes[0, 2].set_title("Ascites")
axes[0, 3].set_title("Hepatomegaly")
axes[1, 0].set_title("Spiders")
axes[1, 1].set_title("Edema")
axes[1, 2].set_title("Stage")

# 隐藏空白子图
axes[1, 3].set_visible(False)

plt.tight_layout()
plt.savefig("cirrhosis_categorical_features.png", dpi=300, bbox_inches='tight')
plt.close()

# 可视化：肝硬化与数值特征的关系
fig, axes = plt.subplots(3, 4, figsize=(24, 18))
sns.histplot(data=df_cirrhosis, x="N_Days", hue="Status", kde=True, ax=axes[0, 0])
sns.histplot(data=df_cirrhosis, x="Age", hue="Status", kde=True, ax=axes[0, 1])
sns.histplot(data=df_cirrhosis, x="Bilirubin", hue="Status", kde=True, ax=axes[0, 2])
sns.histplot(data=df_cirrhosis, x="Cholesterol", hue="Status", kde=True, ax=axes[0, 3])
sns.histplot(data=df_cirrhosis, x="Albumin", hue="Status", kde=True, ax=axes[1, 0])
sns.histplot(data=df_cirrhosis, x="Copper", hue="Status", kde=True, ax=axes[1, 1])
sns.histplot(data=df_cirrhosis, x="Alk_Phos", hue="Status", kde=True, ax=axes[1, 2])
sns.histplot(data=df_cirrhosis, x="SGOT", hue="Status", kde=True, ax=axes[1, 3])
sns.histplot(data=df_cirrhosis, x="Tryglicerides", hue="Status", kde=True, ax=axes[2, 0])
sns.histplot(data=df_cirrhosis, x="Platelets", hue="Status", kde=True, ax=axes[2, 1])
sns.histplot(data=df_cirrhosis, x="Prothrombin", hue="Status", kde=True, ax=axes[2, 2])

# 设置子图标题
axes[0, 0].set_title("N_Days Distribution")
axes[0, 1].set_title("Age Distribution")
axes[0, 2].set_title("Bilirubin Distribution")
axes[0, 3].set_title("Cholesterol Distribution")
axes[1, 0].set_title("Albumin Distribution")
axes[1, 1].set_title("Copper Distribution")
axes[1, 2].set_title("Alk_Phos Distribution")
axes[1, 3].set_title("SGOT Distribution")
axes[2, 0].set_title("Tryglicerides Distribution")
axes[2, 1].set_title("Platelets Distribution")
axes[2, 2].set_title("Prothrombin Distribution")

# 隐藏空白子图
axes[2, 3].set_visible(False)

plt.tight_layout()
plt.savefig("cirrhosis_numerical_features.png", dpi=300, bbox_inches='tight')
plt.close()

print("所有图表已生成完成！")
